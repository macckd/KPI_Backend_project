# DECISIONS.md

## Architecture Rationale

- **Modular App Structure**: The project uses a modular Django structure with `kpis` and `projects` as sub-apps inside a main `app` for clear separation of concerns and future scalability.
- **RESTful API**: Django REST Framework (DRF) is used for rapid API development, leveraging class-based views for explicit control over HTTP methods.
- **Documentation**: `drf-spectacular` is used for OpenAPI schema generation and interactive Swagger UI.

## KPI Flexibility Approach

- KPIs are defined as database models, not hardcoded in code, allowing for flexible addition and modification of KPI types and attributes.
- Each KPI is linked to a project via a ForeignKey, supporting 1:N relationships and enabling project-level KPI summaries.

## Scalability Considerations

- Modular apps allow for easy extension (e.g., adding new modules for users, reports, etc.).
- DRF and Django ORM provide a solid foundation for scaling to more complex business logic and larger datasets.
- API documentation is auto-generated, reducing maintenance overhead as the API evolves.

## Shortcuts & Trade-offs

- **No authentication/authorization**: For simplicity, the current version does not implement user authentication or permissions.
- **SQLite for development**: The default database is SQLite for ease of setup; for production, a more robust DB (e.g., PostgreSQL) is recommended.
- **Minimal validation**: Only basic validation is implemented; business rules can be expanded as requirements grow.
- **No async processing**: All views are synchronous; async support can be added if needed for performance.

## Future Improvements

- Add authentication and permissions (e.g., per-project access control).
- Implement advanced KPI analytics and reporting.
- Support bulk import/export of KPIs and projects.
- Add filtering, searching, and ordering to API endpoints.
- Optimize for large datasets (pagination, query optimization).
- Add automated tests for all endpoints and models.

## References

- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
- [Django Project Structure Best Practices](https://docs.djangoproject.com/en/4.2/intro/reusable-apps/)
