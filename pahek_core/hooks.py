app_name = "pahek_core"
app_title = "PAHEK Core"
app_publisher = "PAHEK Security"
app_description = "Shared foundation for PAHEK Security's Frappe apps: settings, roles, branding"
app_email = "admin@paheksecurity.com"
app_license = "Proprietary"

fixtures = [
	{"dt": "Role", "filters": [["role_name", "in", ["PAHEK Admin", "PAHEK Editor", "AI Drafter"]]]},
]
