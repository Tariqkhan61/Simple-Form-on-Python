import flet as ft

def form_submit_function(e):
    # Basic validation
    first_name = first_name_field.value.strip()
    middle_name = middle_name_field.value.strip()
    last_name = last_name_field.value.strip()
    email = email_field.value.strip()
    password = password_field.value.strip()
    city = city_field.value.strip()
    country = country_field.value.strip()
    
    if not all([first_name, last_name, email, password, city, country]):
        e.page.snack_bar = ft.SnackBar(
            content=ft.Text("Please fill in all required fields!", color="white"),
            bgcolor="#ff4d4d"
        )
        e.page.snack_bar.open = True
        e.page.update()
        return
    
    print("Form submitted with data:")
    print(f"First Name: {first_name}")
    print(f"Middle Name: {middle_name}")
    print(f"Last Name: {last_name}")
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)}")
    print(f"City: {city}")
    print(f"Country: {country}")
    
    # Show success message
    e.page.snack_bar = ft.SnackBar(
        content=ft.Text("Form submitted successfully!", color="white"),
        bgcolor="#4CAF50"
    )
    e.page.snack_bar.open = True
    
    # Clear form fields
    first_name_field.value = ""
    middle_name_field.value = ""
    last_name_field.value = ""
    email_field.value = ""
    password_field.value = ""
    city_field.value = ""
    country_field.value = ""
    
    e.page.update()

# Create form fields with THICKER BORDERS (border_width=3)
first_name_field = ft.TextField(
    label="First Name", 
    text_size=16, 
    border_radius=14,
    focused_border_color="#6200EE",
    color="#333333",
    cursor_color="#6200EE",
    border_width=2,  # Changed from 1 to 3
    border_color="#6200EE",
    filled=True,
    fill_color="#F3E5F5"
)

middle_name_field = ft.TextField(
    label="Middle Name (Optional)", 
    text_size=16, 
    border_radius=14,
    focused_border_color="#6200EE",
    color="#333333",
    cursor_color="#6200EE",
    border_width=2,  # Changed from 1 to 3
    border_color="#6200EE",
    filled=True,
    fill_color="#F3E5F5"
)

last_name_field = ft.TextField(
    label="Last Name", 
    text_size=16, 
    border_radius=14,
    focused_border_color="#6200EE",
    color="#333333",
    cursor_color="#6200EE",
    border_width=2,  # Changed from 1 to 3
    border_color="#6200EE",
    filled=True,
    fill_color="#F3E5F5"
)

email_field = ft.TextField(
    label="Email", 
    text_size=16, 
    border_radius=14,
    focused_border_color="#6200EE",
    color="#333333",
    cursor_color="#6200EE",
    border_width=2,  # Changed from 1 to 3
    border_color="#6200EE",
    filled=True,
    fill_color="#E3F2FD"
)

password_field = ft.TextField(
    label="Password", 
    password=True, 
    can_reveal_password=True,
    text_size=16, 
    border_radius=14, 
    focused_border_color="#6200EE",
    color="#333333", 
    cursor_color="#6200EE", 
    border_width=2,  # Changed from 1 to 3
    border_color="#6200EE",
    filled=True,
    fill_color="#E3F2FD"
)

city_field = ft.TextField(
    label="City", 
    text_size=16, 
    border_radius=14,
    focused_border_color="#6200EE",
    color="#333333",
    cursor_color="#6200EE",
    border_width=2,  # Changed from 1 to 3
    border_color="#6200EE",
    filled=True,
    fill_color="#E8F5E9"
)

country_field = ft.TextField(
    label="Country", 
    text_size=16, 
    border_radius=14,
    focused_border_color="#6200EE",
    color="#333333",
    cursor_color="#6200EE",
    border_width=2,  # Changed from 1 to 3
    border_color="#6200EE",
    filled=True,
    fill_color="#E8F5E9"
)

# Form container with THICKER BORDER (border=ft.border.all(4, "#6200EE"))
form_container = ft.Container(
    content=ft.Column(
        [
            ft.Text("Sign Up Form", 
                   size=30, 
                   color="#6200EE", 
                   weight="bold",
                   text_align="center"),
            first_name_field,
            middle_name_field,
            last_name_field,
            email_field,
            password_field,
            city_field,
            country_field,
            ft.Container(
                content=ft.ElevatedButton(
                    text="Submit", 
                    color="white", 
                    bgcolor="#6200EE",
                    width=200, 
                    height=45, 
                    on_click=form_submit_function,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=20),  # Increased radius
                        elevation=5,
                        side=ft.BorderSide(5, "#6200EE")  # Added border to button
                    )
                ),
                margin=ft.margin.only(top=20)
            )
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=12
    ),
    width=450,
    padding=30,
    bgcolor=ft.colors.with_opacity(0.95, "#FFFFFF"),
    border_radius=20,
    border=ft.border.all(6, "orange"),  # Changed from 2 to 4
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=["#F3E5F5", "#E3F2FD", "#E8F5E9"]
    ),
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=15,
        color=ft.colors.with_opacity(0.2, "#6200EE"),
        offset=ft.Offset(0, 5)
    )
)

def main(page: ft.Page):
    page.title = "Sign Up Form"
    page.window_width = 900
    page.window_height = 800
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.bgcolor = "#F5F5F5"
    
    page.add(
        ft.Column(
            [form_container],
            alignment="center",
            horizontal_alignment="center",
            spacing=0
        )
    )

ft.app(target=main)