import type { User } from './user.ts';
import type { Comment } from './comment.ts';
import type { Timestamp } from './common.ts';

export interface Post extends Timestamp {
  id: number;
  title: string;
  body: string;
  user: User;
  comments: Comment[];
}

export interface UpdatePostDTO {
  title: string;
  body: string;
}

export interface UpdatePostPayload {
  id: number;
  data: UpdatePostDTO;
}

export type PostSort = 'none' | 'title' | 'comments';
