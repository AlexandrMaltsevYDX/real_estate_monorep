import { ReactNode, DetailedHTMLProps, HTMLAttributes } from 'react';

import { ReviewInterface } from '~interfaces/review.interface';

export interface ReviewsBlockProps extends DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement> {
  reviewsDataItem: ReviewInterface[]; //reviewDataInterface[]
  children?: ReactNode;
}
