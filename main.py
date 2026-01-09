def generate_html(name):
    return f"<html><body><h1>Hello {name}! CI/CD is working!</h1></body></html>"

if __name__ == "__main__":
    print(generate_html("Developer"))