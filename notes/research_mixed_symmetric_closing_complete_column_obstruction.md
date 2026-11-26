# The actual complete Newton column exceeds the proposed two-crossing rate

Private written source deduction, 9 November 2026. The vector considered
here is exactly the original crossing matrix applied to the complete
Newton evaluation vector. A single physical midpoint row has a larger
exponential rate than the proposed ceiling \(b_2\). This rules out that
particular norm shortcut for the remaining closing current. It gives
no lower bound for the signed current itself.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, test or frozen-source edit is used.

## 1. The exact vector and its physical midpoint row

Keep the original conventions
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \kappa=q^{D^2/2},\quad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\quad S_0=1,
\]
\[
 e_j(w)=S_j^{-2}\prod_{\nu<j}(c_\nu-w),\qquad
 c_\nu=2\cos((2\nu+1)\pi/N),\qquad
 \mathbf e(w)=(e_0(w),\ldots,e_D(w))^T .                 \tag{1}
\]
The vector \(\mathbf e(-2)\) in (1) is an evaluation vector; it is
not the coordinate unit vector \(\mathbf e_0\). The complete
crossing matrix is
\[
 M_{j\ell}=\kappa(-1)^j q^{j(\ell+1)}
                  \frac{S_j}{S_\ell S_{j-\ell}},
                  \qquad0\le\ell\le j<N .                       \tag{2}
\]
All other entries vanish. This is the original full Hermite-algebra
matrix, not its value-only quotient or an asymptotic replacement.

Set \(E_\ell=e_\ell(-2)\) and retain the original complete-boundary
coefficient
\[
 C_{j,N}=\sum_{\ell=0}^j
          \frac{q^{j\ell}E_\ell}{S_\ell S_{j-\ell}} .            \tag{3}
\]
Directly from (2), at every level and every row,
\[
             (M\mathbf e(-2))_j
                       =\kappa(-q)^j S_j C_{j,N}.               \tag{4}
\]
This is also the exact ordinary-color transform identity
\((M\mathbf e(w))_j=\kappa(-q)^j\mathcal H_N(w,r^{-j})\),
with \(r=q^{-2}\): at \(w=-2\), its original normalization is
\(\mathcal H_N(-2,r^{-j})=S_j C_{j,N}\).
Thus
\[
       \|M\mathbf e(-2)\|_2^2
                         =\sum_{j=0}^{D}S_j^2|C_{j,N}|^2 .      \tag{5}
\]
Neither a left-eigenvector identity for \(\mathbf e(-2)^TM\) nor
the different column \(MJM^3\mathbf e_0\) changes (4)--(5).

Let \(m_N=\lfloor N/2\rfloor\). The exact sine-product reflection
gives
\[
 S_{m_N}=
 \begin{cases}
  \sqrt{2N},&N\text{ even},\\
  \sqrt N,&N\text{ odd}.
 \end{cases}                                                    \tag{6}
\]
Indeed \(S_D=N\); pair equal sine factors around \(N/2\), with
the additional factor two at the midpoint when \(N\) is even.
All factors in (3) at this row are nonzero denominators. At odd
levels an original Newton numerator zero remains a zero and has
not been divided out.

## 2. The original nonzero cap packet at the midpoint

Use the calibrated primitive on \(0<\Re z<1\),
\[
 J(z)=\int_0^z\Log(2\sin\pi w)\,dw,
\]
continued from the real interval, and the full-index cap phase
\[
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,
\]
\[
 u_c(e)=\frac1\pi\arctan
                 \frac{i+\sqrt{1-2e^{2\pi ie}}}{2},\qquad
 S_{\rm cap}(e)=F(e,u_c(e)),\quad
 \lambda(e)=\Re S_{\rm cap}(e).                                 \tag{7}
\]
These are the original branches, including the zero logarithmic
lift and additive constant. The adopted full-index theorem proves,
uniformly on every compact real interval about \(e=1/2\),
\[
 C_{j,N}=N^{-3/2}A_0(j/N)e^{NS_{\rm cap}(j/N)}
                                  (1+O(N^{-1})),\qquad A_0\ne0.\tag{8}
\]
It is a theorem for the actual sum (3), at both parities, with
all its physical rows and reciprocal-factorial continuations.
In particular, it licenses the moving physical row
\[
 \frac{m_N}{N}=
 \begin{cases}
  1/2,&N\text{ even},\\
  1/2-1/(2N),&N\text{ odd}.
 \end{cases}                                                    \tag{9}
\]
Holomorphy and nonvanishing in (8) show that this shift changes
the real exponential by only a bounded factor and the amplitude
by \(1+O(N^{-1})\). Equations (4),(6),(8) therefore give constants
\(c_*>0\) and \(N_*>0\), uniform over both parities, such that
\[
 \boxed{\qquad
 \|M\mathbf e(-2)\|_2
       \ge |(M\mathbf e(-2))_{m_N}|
       \ge c_*N^{-1}e^{N\lambda(1/2)}\qquad(N\ge N_*).
 \qquad}                                                       \tag{10}
\]
Only one of the nonnegative terms in the exact norm (5) is used.
No cancellation claim for a later bilinear observation follows.

## 3. A written strict comparison with \(b_2\)

The original two-crossing constant is
\[
 b_2=-4J(1/4)=\frac{2G}{\pi},\qquad
 G=\sum_{k\ge0}\frac{(-1)^k}{(2k+1)^2}.                         \tag{11}
\]
At \(e=1/2\), the exact critical point in (7) is
\[
 u_c(1/2)=1/4+ih_*,\qquad h_*=\frac{\log3}{4\pi}>0 .           \tag{12}
\]
For \(0\le h\le h_*\), set
\(L(h)=\Re F(1/2,1/4+ih)\). Since
\(J(\overline z)=\overline{J(z)}\) on this original strip,
\[
 L(h)=-6\Re J(1/4+ih)-\pi h/2,\qquad
 L(0)=\frac32b_2.                                              \tag{13}
\]
The first-quadrant sine has argument
\(\arctan(\tanh\pi h)\). Differentiating (13) gives exactly
\[
 L'(h)=6\arctan(\tanh\pi h)-\pi/2.                            \tag{14}
\]
At \(h=h_*\),
\[
 \tanh(\pi h_*)=2-\sqrt3=\tan(\pi/12),
\]
so (14) increases from \(-\pi/2\) to zero, and is strictly
greater than \(-\pi/2\) for \(h>0\). Integrating over the literal
segment in (12), with no change of primitive, proves
\[
 \lambda(1/2)=L(h_*)>
                      \frac32b_2-\frac{\log3}{8}.              \tag{15}
\]

Here are elementary rational witnesses for the desired strict gap.
The alternating series gives \(G>1-1/9=8/9\); with
\(\pi<22/7\), this implies \(b_2>56/99\).
Also
\[
 e^{4/3}>1+4/3+(4/3)^2/2=29/9>3,
\]
hence \(\log3<4/3\). Consequently
\[
 \lambda(1/2)-b_2
 >\frac{b_2}{2}-\frac{\log3}{8}
 >\frac{28}{99}-\frac16
 =\frac{23}{198}>\frac19 .                                    \tag{16}
\]
No numerical value of the cap action is used.

Combining (10) and (16) proves that no fixed constants \(C,A\)
can make
\[
                  \|M\mathbf e(-2)\|_2\le CN^A e^{Nb_2}        \tag{17}
\]
hold for all sufficiently large levels, at either parity. The
excess in (16) dominates every fixed polynomial.

## 4. Scope for the remaining closing problem

The existing full-matrix estimate
\(\|M^2\|_2\le CN^A e^{Nb_2}\) is unchanged. One may still use
\(\|M^3\mathbf e(-2)\|_2\le\|M^2\|_2\|M\mathbf e(-2)\|_2\),
but the second factor cannot be assigned the rate \(b_2\).
This note does not prove a sharp upper rate for that factor,
or an obstruction to every refined estimate for \(M^3\mathbf e(-2)\).

In particular the signed outer closing current contains further
matrix contractions, crossing phases, full trace normals and its
sampling denominator. Its rate cannot be bounded below by the
single coefficient in (10). No failure of that current, of the
closing asymptotic, or of short-partial-filling stability is inferred.

## Frozen source bindings

- Original complete crossing matrix and distinction from the next
  prepared column:
  [next-step source](research_three_crossing_next_step_profile.md),
  b5343394936f80cc255cfa37ec5f410e29a453495b93bc2e1f538238199a1eac.
- Exact ordinary-color transform, with its left-versus-right warning:
  [terminal color transform](research_mixed_terminal_color_transform.md),
  50ae32721808604cf1a64c060013c0392be0ab4f5bb812627ab606ffe63b6713.
- Complete physical full-index cap packet, including the midpoint and
  both level parities:
  [full-index coefficient theorem](research_complete_boundary_full_index_interval.md),
  450cd41db9c49049e9b80a41c83828a2f0fafa43f986803bc57b93be580a57ef.
- Original two-crossing constant, full-matrix bound and Newton vector:
  [preparation-error source](research_three_crossing_global_preparation_error.md),
  c1e80c6efbc9ff936d889eebd1f449e85c81820a64fb046e6dfe8e1003d2d239.
