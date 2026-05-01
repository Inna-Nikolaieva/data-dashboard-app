import apiClient from './client.ts';
import { COMMENTS } from './routes.ts';
import type { UpdateCommentDTO, Comment } from '../types/comment.ts';

export const CommentsApi = {
  updateComment: (
    commentId: number,
    data: UpdateCommentDTO
  ): Promise<Comment> =>
    apiClient
      .put(COMMENTS.updateComment(commentId), data)
      .then((res) => res.data),

  deleteComment: (commentId: number): Promise<void> =>
    apiClient.delete(COMMENTS.deleteComment(commentId)).then((res) => res.data),
};
