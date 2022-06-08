"""User manager."""

from typing import Any

from multiauth.helpers import jwt_token_analyzer
from multiauth.types.errors import AuthenticationError
from multiauth.types.main import AuthTech, AuthType, JWTToken, Token, UserBase


# pylint: disable=too-many-instance-attributes
class User(UserBase):

    """User entity."""

    def __init__(self, kwargs: dict[str, Any] | None = None) -> None:
        """Init user."""

        self.reset()

        if kwargs:
            for key, value in kwargs.items():
                if not key.startswith('_'):
                    key = '_' + key
                setattr(self, key, value)

    def reset(self) -> None:
        """Reset user."""

        self._auth_schema: str | None = None
        self._auth_tech: AuthTech = AuthTech.NOAUTH
        self._auth_type: AuthType | None = None
        self._credentials: dict[str, Any] | None
        self._expired_token: Token | None = None
        self._expires_in: float | None = None
        self._refresh_token: Token | None = None
        self._token_info: JWTToken | None = None
        self._token: Token | None = None

    @property
    def auth_schema(self) -> str | None:
        """Get auth schema."""

        return self._auth_schema

    @property
    def auth_tech(self) -> AuthTech:
        """Get auth tech."""

        return self._auth_tech

    @property
    def auth_type(self) -> AuthType | None:
        """Get the authentication type."""

        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type: AuthType | None) -> None:
        """Set the authentication type."""

        self._auth_type = auth_type

    @property
    def credentials(self) -> dict[str, Any] | None:
        """Get credentials."""

        return self._credentials

    @property
    def expired_token(self) -> Token | None:
        """Get the expired token."""

        return self._expired_token

    @expired_token.setter
    def expired_token(self, token: Token | None) -> None:
        """Set the expired token."""

        self._expired_token = token

    @property
    def expires_in(self) -> float | None:
        """Get the expiration time."""

        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in: float | None) -> None:
        """Set the expiration time."""

        self._expires_in = expires_in

    @property
    def refresh_token(self) -> Token | None:
        """Get the refresh token."""

        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, token: Token | None) -> None:
        """Set the refresh token."""

        self._refresh_token = token

    @property
    def token_info(self) -> JWTToken | None:
        """Get the token info."""

        return self._token_info

    @token_info.setter
    def token_info(self, token: JWTToken | None) -> None:
        """Set the token info."""

        self._token_info = token

    @property
    def token(self) -> Token | None:
        """Get the token."""

        return self._token

    @token.setter
    def token(self, token: Token | None) -> None:
        """Set the token."""

        self._token = token

    def set_token(self, token: Token | None, expires_in: float | None) -> None:
        """Set token."""

        self.token = token
        self.expires_in = expires_in

        if token:
            try:
                self.token_info = jwt_token_analyzer(token)
            except AuthenticationError:
                pass

    def get_credentials(self) -> tuple[str, str]:
        """Get credentials."""

        if not self.credentials:
            raise AuthenticationError('Missing credentials.')
        if not self.credentials.get('username'):
            raise AuthenticationError('Please provide a username')
        if not self.credentials.get('password'):
            raise AuthenticationError('Please provide a password')

        return self.credentials['username'], self.credentials['password']


class UserManager:

    """User manager."""

    _users: dict[str, User]

    def __init__(
        self,
        users: dict[str, User] | None = None,
    ) -> None:
        """Initialize the User manager."""

        if not users:
            users = {}

        self._users: dict[str, User] = users

    def reset(self) -> None:
        """Reset the user manager."""

        self._users = {}

    @property
    def users(self) -> dict[str, User]:
        """Get all users."""

        return self._users
