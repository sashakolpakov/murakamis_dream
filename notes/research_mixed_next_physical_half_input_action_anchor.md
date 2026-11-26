# The half-input action comparison from an original physical summand

Private research theorem, 9 November 2026. The first physical summand
in the right half of the original transfer already has an exponential
gap. The newly proved nonzero Fourier asymptotic and the outgoing
polynomial's absolute rate turn that finite estimate into the
correlated action inequality needed at zero Fourier frequency.
No numerical evaluation or change to a frozen source is used.

## 1. Original source and reference family

Consider an actual complete word in powers three and four beginning
\(343\), of length at least five. Keep its original coupled reference
and outgoing coordinate \(z_*\), with
\[
 Z_*=e^{-2\pi iz_*},\qquad
 \Lambda=\Re\mathcal P_0^+(-2,z_*)
         =\Lambda_{123}(z_*).
 \tag{1}
\]
These are the reference family and the absolute action used in
[the physical half-band theorem](research_mixed_next_three_physical_half_band_from_vertical.md),
Section 4. Its parameters and its original ordinary color \(w=-2\)
are retained.

Write
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa_N=q^{D^2/2},\quad M=\lceil N/2\rceil,\quad
 U=D-M,\quad P_b=(r;r)_b .
 \tag{2}
\]
The complete outgoing polynomial is
\[
 C_{b,N}(Z)=C_{0,N}(r^b,Z)
  =\sum_{j=0}^{D-b}
       \frac{r^{-bj}(r^{b+1};r)_j(rZ;r)_j}{(r;r)_j^2}.
 \tag{3}
\]
All its physical stopping factors are kept. The
[absolute-anchor theorem](research_mixed_next_outgoing_absolute_anchor.md)
defines its real action \(\mathcal E(a,Z)\), normalized by the
literal terminal row \(C_{D,N}=1\). Put
\[
 E_0(Z)=\mathcal E(1/2,Z).
 \tag{4}
\]
On the eligible actual output region, the terminal-normalization
theorem identifies this with the original outgoing action.

Retain the exact full Hermite kernel
\[
 \mathcal K_{3,N}(w,x)
   =\phi_N^{(t)}[R_N(t)^3K_N(w,t)K_N(x,t)].
 \tag{5}
\]
Equation (3) of
[the original high-coefficient theorem](research_mixed_next_high_coefficients_terminal_insertion.md)
gives
\[
 \ell_b(w)
   =\phi_N^{(x)}[\mathcal K_{3,N}(w,x)e_b(x)R_N(x)^3].
 \tag{6}
\]
The first normals at double roots are part of this identity.

## 2. Statement

Let \(\Gamma(\delta)\) be the real part of the original selected
outer action in
[the whole Fourier theorem](research_mixed_next_whole_outer_fourier_asymptotic.md).
Then, uniformly on the actual references above,
\[
 \boxed{\quad
 E_0(Z_*)+\Gamma(1/2)
       \le \Lambda-\frac{1}{2\cdot10^{13}}.
 \quad}
 \tag{7}
\]
Thus the zero-frequency action comparison has a fixed strict gap.
This conclusion does not replace \(\Gamma(1/2)\) by the larger
complete inner action \(M_3\).

## 3. Proof from the exact physical node

The original full observation is
\[
 \mathcal O_{N,k}
   =\phi_N[R_N^3e_M\widehat Q_N^{\rm full}T_k(-\,\cdot/2)].
 \tag{8}
\]
Here \(\widehat Q_N^{\rm full}(x)=\mathcal K_{3,N}(-2,x)\),
and \(T_0=1\). Equations (5)--(8) therefore give the exact identity
\[
                         \ell_M(-2)=\mathcal O_{N,0}.
 \tag{9}
\]
No shortening, new normalization, or asymptotic step is used in (9).

In the physical half-band theorem, take the unfiltered polynomial
\(G_N=F_{34,N}\), ordinary color \(w=-2\), outgoing value \(Z_*\),
and the singleton set of physical indices \(\{M\}\). This index is
in that theorem's fixed-width band for all sufficiently large \(N\)
at either parity. Its equations (17)--(18) yield
\[
 \left|\frac{(-q)^M}{\kappa_N^2N}
              \ell_M(-2)C_{M,N}(Z_*)\right|
  \le CN^A
     \exp N\left\{\Lambda-\frac{1}{2\cdot10^{13}}\right\}.
 \tag{10}
\]
This is an estimate of the original physical summand with its
outgoing factor already included.

The whole Fourier theorem applies at \(k=0\), hence
\(\delta=1/2\), and its nonzero coefficient gives
\[
 |\mathcal O_{N,0}|
       \ge cN^{-1}e^{N\Gamma(1/2)}
 \tag{11}
\]
for all sufficiently large \(N\) of both parities. In particular,
its two reflected contributions reinforce each other; their exact
factor is two.

The complete outgoing absolute-anchor theorem, equation (10),
gives
\[
 \log|C_{M,N}(Z_*)|
      =N\mathcal E(M/N,Z_*)+O(\log N)
      =NE_0(Z_*)+O(\log N).
 \tag{12}
\]
The last equality retains the odd shift:
\(M/N=1/2+1/(2N)\) at odd levels and \(M/N=1/2\) at even
levels. The action derivative \(\log|\mathcal L(a,Z)|\) is uniformly
bounded on a fixed neighborhood of \(a=1/2\), by the nonzero
continuous selected ratio on the compact output region. Thus this
shift contributes \(O(1)\) in the exponent, uniformly.

Since \(|q|=|\kappa_N|=1\), equations (9),(11),(12) bound the
left side of (10) from below by
\[
 c'N^{-B}\exp N\{\Gamma(1/2)+E_0(Z_*)\}
 \tag{13}
\]
with fixed constants. Taking logarithms of (10),(13), dividing by
\(N\), and letting \(N\) tend to infinity proves (7). No
lower bound for a signed sum was inferred from an upper bound:
the lower bounds in (11),(12) are separate proved source results.
\(\square\)

## 4. Consequence and remaining comparison

Let \(\mathcal D(t,Z_*)\) be the outgoing Fourier coefficient
upper rate defined by the positive transition theorem, where
\(t=k/N\). It has the exact endpoint value
\[
 \mathcal D(0,Z_*)=E_0(Z_*).
 \tag{14}
\]
Consequently (7) controls the combined rate at \(t=0\).
If a further estimate proves
\[
 \mathcal D(t,Z_*)+\Gamma(1/2-t)
       \le E_0(Z_*)+\Gamma(1/2)
       \qquad (0\le t\le1/2),
 \tag{15}
\]
then the whole combined action envelope is below \(\Lambda\)
by the fixed gap in (7). Equation (15) is a separate
comparison, not a consequence of the physical-node bound alone.
The finite high-frequency endpoint still uses its original
terminal-mode theorem when the fixed-\(\delta_1\) Fourier theorem
is applied.

The present theorem concerns these actual complete references at
\(w=-2\). It does not extend the whole Fourier asymptotic to a
complex neighborhood in \(w\), prove every short partial filling,
or establish the finite-exception target.

## Source versions

- Original high coefficient as the full Hermite trace:
  eac17dec814ff750bd1845fd84b935058f4f10206eefd281e5124bd19efc5c09.
- Physical half-band and exact unfiltered summand:
  49742a29c50971279920522fb231f8950ca91d0a54bc6a7245f29672f13c8a8d.
- Whole Fourier coefficient, including zero frequency:
  8c0f4853c05443eb76d821bca6d7248f6c00e19177a796e530e4b4cd24d93ac6.
- Complete outgoing absolute rate and nonvanishing:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Original outgoing action normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
