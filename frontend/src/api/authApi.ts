import apiClient from './client.ts';
import { AUTH } from './routes.ts';
import type { LoginRequest, LoginResponse, BaseUser } from '../types/user.ts';

export const AuthApi = {
  login: (data: LoginRequest): Promise<LoginResponse> =>
    apiClient.post(AUTH.login(), data).then((res) => res.data),

  currentUser: (token: string): Promise<BaseUser> =>
    apiClient
      .get(AUTH.currentUser(), {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((res) => res.data),
};
