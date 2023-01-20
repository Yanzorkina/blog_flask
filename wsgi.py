import os

from blog.app import app
from blog.models.database import db
from blog.models import User

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )

@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User

    admin = User(username="admin_terminal", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    db.session.add(admin)
    db.session.commit()
    print("created admin:", admin)


