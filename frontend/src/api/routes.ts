export const DUMMY_DATA = {
  importData: () => '/import-dummy-data',
};

export const AUTH = {
  login: () => 'https://dummyjson.com/user/login',
  currentUser: () => 'https://dummyjson.com/user/me',
};

export const POSTS = {
  getAllPosts: () => '/posts',
  getPost: (postId: number) => `/posts/${postId}`,
  updatePost: (postId: number) => `/posts/${postId}`,
  deletePost: (postId: number) => `/posts/${postId}`,
};

export const COMMENTS = {
  updateComment: (commentId: number) => `/comments/${commentId}`,
  deleteComment: (commentId: number) => `/comments/${commentId}`,
};
