import apiClient from './client.ts';
import { POSTS } from './routes.ts';
import type { Post, UpdatePostDTO } from '../types/post.ts';

export const PostsApi = {
  getAllPosts: (): Promise<Post[]> =>
    apiClient.get(POSTS.getAllPosts()).then((res) => res.data),

  getPostById: (postId: number): Promise<Post> =>
    apiClient.get(POSTS.getPost(postId)).then((res) => res.data),

  updatePost: (postId: number, data: UpdatePostDTO): Promise<Post> =>
    apiClient.put(POSTS.updatePost(postId), data).then((res) => res.data),

  deletePost: (postId: number): Promise<void> =>
    apiClient.delete(POSTS.deletePost(postId)).then((res) => res.data),
};
