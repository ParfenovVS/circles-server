from firebase_functions import identity_fn, https_fn
from firebase_admin import auth, firestore, initialize_app

initialize_app()


@identity_fn.before_user_created()
def create_user(
    event: identity_fn.AuthBlockingEvent
) -> identity_fn.BeforeCreateResponse | None:
    pass
