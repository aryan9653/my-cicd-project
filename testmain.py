from main import generate_html  # Removed the ".py"

def test_output():
    assert "CI/CD is working!" in generate_html("User")