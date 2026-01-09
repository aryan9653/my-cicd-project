from main.py import generate_html

def test_output():
    # This test ensures our HTML generator works correctly
    assert "CI/CD is working!" in generate_html("User")