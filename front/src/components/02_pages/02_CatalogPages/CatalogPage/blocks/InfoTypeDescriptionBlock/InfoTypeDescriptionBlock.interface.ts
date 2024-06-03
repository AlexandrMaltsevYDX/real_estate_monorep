import { DetailedHTMLProps, HTMLAttributes } from 'react';

export interface InfoTypeDescriptionBlockInterface extends DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement> {
  typePage: 'flats' | 'lands' | 'houses-and-cottages' | 'villages';
}
