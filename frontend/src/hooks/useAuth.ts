import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { AuthApi } from '../api/authApi';
import type { BaseUser, LoginRequest, LoginResponse } from '../types/user.ts';

const TOKEN_KEY = 'token';

export const useAuth = () => {
  const queryClient = useQueryClient();

  const token = localStorage.getItem(TOKEN_KEY);

  const login = useMutation<LoginResponse, Error, LoginRequest>({
    mutationFn: AuthApi.login,
    onSuccess: (data) => {
      const accessToken = data.accessToken;

      localStorage.setItem(TOKEN_KEY, accessToken);

      queryClient.invalidateQueries({ queryKey: ['currentUser'] });
    },
  });

  const currentUser = useQuery<BaseUser | null>({
    queryKey: ['currentUser'],
    queryFn: () => {
      if (!token) return null;
      return AuthApi.currentUser(token);
    },
    enabled: !!token,
  });

  const logout = () => {
    localStorage.removeItem(TOKEN_KEY);
    queryClient.setQueryData(['currentUser'], null);
  };

  return {
    user: currentUser.data,
    isLoading: currentUser.isLoading,
    login: login.mutateAsync,
    logout,
    token,
  };
};
