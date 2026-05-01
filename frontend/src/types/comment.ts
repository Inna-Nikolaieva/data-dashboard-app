import type { User } from './user.ts';

export interface Comment {
  id: number;
  createdAt: string;
  updatedAt: string;
  body: string;
  user: User;
}

export interface UpdateCommentDTO {
  body: string;
}

export interface UpdateCommentPayload {
  id: number;
  data: UpdateCommentDTO;
}
