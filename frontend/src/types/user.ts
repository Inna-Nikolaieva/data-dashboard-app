import type { Timestamp } from './common.ts';

export interface BaseUser {
  id: number;
  username: string;
  email: string;
}

export interface User extends Timestamp, BaseUser {}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  accessToken: string;
  user: BaseUser;
}
