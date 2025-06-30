import { describe, it, expect } from 'vitest';
import { render } from 'astro/test';
import Footer from '../src/components/Footer.astro';

describe('Footer.astro', () => {
  it('muestra el número de teléfono', async () => {
    const result = await render(Footer);
    expect(result.html()).toContain('201-755-7836');
  });
});