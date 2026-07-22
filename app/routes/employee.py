from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.models import db
from app.models.employee import Employee

employee_bp = Blueprint("employee", __name__)

PER_PAGE = 5


def _get_filter_query():
    query = Employee.query

    search_term = request.args.get("search", "").strip()
    if search_term:
        like_term = f"%{search_term}%"
        query = query.filter(
            db.or_(
                Employee.name.ilike(like_term),
                Employee.email.ilike(like_term),
                Employee.department.ilike(like_term),
            )
        )

    department = request.args.get("department", "").strip()
    if department:
        query = query.filter(Employee.department == department)

    min_salary_raw = request.args.get("min_salary", "").strip()
    if min_salary_raw:
        try:
            min_salary = float(min_salary_raw)
        except ValueError:
            min_salary = None
        if min_salary is not None:
            query = query.filter(Employee.salary >= min_salary)

    max_salary_raw = request.args.get("max_salary", "").strip()
    if max_salary_raw:
        try:
            max_salary = float(max_salary_raw)
        except ValueError:
            max_salary = None
        if max_salary is not None:
            query = query.filter(Employee.salary <= max_salary)

    sort_by = request.args.get("sort_by", "name").strip().lower()
    sort_order = request.args.get("sort_order", "asc").strip().lower()

    if sort_by not in {"name", "email", "department", "salary"}:
        sort_by = "name"
    if sort_order not in {"asc", "desc"}:
        sort_order = "asc"

    sort_column = getattr(Employee, sort_by)
    if sort_order == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    return query


@employee_bp.route("/employee/<int:id>/<string:name>")
def searchByNameId(id, name):
    return f"ID : {id} Name : {name}"


@employee_bp.route("/employee")
def displaySpecific():
    return redirect(url_for("employee.employee_list"))


@employee_bp.route("/employeeDepartment")
def gotodept():
    return redirect(url_for("department.departmentHome"))


@employee_bp.route("/employee/register")
def register_employee():
    return render_template("add_employee.html")


@employee_bp.route("/employee/list")
def employee_list():
    query = _get_filter_query()

    page = request.args.get("page", 1, type=int)
    page = max(page, 1)

    pagination = query.paginate(page=page, per_page=PER_PAGE, error_out=False)
    if pagination.pages and page > pagination.pages:
        pagination = query.paginate(page=pagination.pages, per_page=PER_PAGE, error_out=False)

    employees = pagination.items
    departments = [
        item[0]
        for item in db.session.query(Employee.department).distinct().order_by(Employee.department).all()
    ]

    query_params = request.args.to_dict(flat=True)
    query_params.pop("page", None)

    page_numbers = []
    if pagination.pages > 1:
        start_page = max(1, pagination.page - 2)
        end_page = min(pagination.pages, pagination.page + 2)
        page_numbers = list(range(start_page, end_page + 1))

    return render_template(
        "employee.html",
        employees=employees,
        pagination=pagination,
        page_numbers=page_numbers,
        departments=departments,
        query_params=query_params,
        search=request.args.get("search", "", type=str).strip(),
        department=request.args.get("department", "", type=str).strip(),
        min_salary=request.args.get("min_salary", "", type=str).strip(),
        max_salary=request.args.get("max_salary", "", type=str).strip(),
        sort_by=request.args.get("sort_by", "name", type=str).strip().lower(),
        sort_order=request.args.get("sort_order", "asc", type=str).strip().lower(),
    )


@employee_bp.route("/employee/add", methods=["POST", "GET"])
def employeeAdd():
    if request.method == "POST":
        employee = Employee(
            name=request.form["name"],
            email=request.form["email"],
            password=request.form["password"],
            salary=request.form["salary"],
            department=request.form["department"],
        )

        db.session.add(employee)
        db.session.commit()
        flash("Employee added successfully.", "success")

        return redirect(url_for("employee.employee_list"))

    return render_template("add_employee.html")


# get specific employee
@employee_bp.route("/employee/employeeDetail/<int:id>", methods=["GET"])
def employeeDetail(id):
    employee = Employee.query.get_or_404(id)
    return render_template("employee_detail.html", employee=employee)


@employee_bp.route("/employee/employeeUpdate/<int:id>", methods=["POST", "GET"])
def employeeUpdate(id):
    employee = Employee.query.get_or_404(id)

    if request.method == "POST":
        employee.name = request.form["name"]
        employee.email = request.form["email"]
        employee.password = request.form["password"]
        employee.salary = request.form["salary"]
        employee.department = request.form["department"]

        db.session.commit()
        flash("Employee updated successfully.", "success")

        return redirect(url_for("employee.employee_list"))

    return render_template("update_employee.html", employee=employee)


@employee_bp.route("/employee/employeeDelete/<int:id>")
def employeeDelete(id):
    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()
    flash("Employee deleted successfully.", "success")

    return redirect(url_for("employee.employee_list"))
