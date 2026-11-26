# The shortened second edge with no internal real cut

Private exact source assembly, 8 November 2026. No mathematical
numerical evaluation or frozen-source edit is used.

The left and right physical endpoint intervals of the shortened
second edge are already below the selected action. They permit
a contour for the entire intervening finite sum with only two
external vertical sides. In particular no vertical side at the
old first-quarter right cut survives. That side cannot be bounded
separately at the required rate.

The resulting formula isolates the known Gaussian integral and
leaves two explicit continued contour integrals. All original
reciprocal-factorial branches and Fourier corrections are contained
in their exact integrands. No bound for those two integrals is
asserted.

## 1. The unchanged finite kernel and interpolation

Let \(u\) range over the compact actual family
\[
 \mathcal U_+=\{0\le\Re u\le\pi/2,\ -1/2\le\Im u\le0\},
\]
and let \(t=t(u)\) be the selected branch of
[the cubic continuation theorem](research_mixed_next_inner_three_cubic_continuation.md).
Use the ordinary original polynomials
\[
 e_j(\xi)=S_j^{-2}\prod_{\nu<j}(c_\nu-\xi),\qquad
 c_\nu=2\cos((2\nu+1)\pi/N),\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N).
\]
The exact [outer annihilator](research_mixed_next_outer_exact_low_edge_reduction.md)
permits the second edge
\[
 K_N^{<}(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),
 \qquad U=\lfloor N/2\rfloor-1 .
\tag{1}
\]
This cutoff includes precisely the eligible rows at both level
parities. It is not a change of the complete inner trace.

Keep the canonical factorial \(G_N\) and its exact Newton
interpolation
\[
 B_N(y,a)=
 \frac{N}{
 G_N(N(1/2-y+a/(2\pi))-1/2)
 G_N(N(1/2-y-a/(2\pi))-1/2)G_N(Ny)^2},
\]
\[
                      T_N(y;t,u)=B_N(y,t)B_N(y,u).
\tag{2}
\]
Then \(T_N(j/N;t,u)\) is the summand in (1) exactly.
These formulas and their complete normalization are proved in
[the original factorial interpolation](exact_factorial_interpolation_and_complex_contours.md)
and [the uniform factorial theorem](research_uniform_factorial_and_boundary_decay.md).

For fixed actual parameters, \(T_N\) is holomorphic throughout
\[
                         0<\Re y<1/2 .
\tag{3}
\]
Here and below holomorphy means at every finite imaginary height.
To check (3), the two shifted factorial real arguments in
\(B_N(y,a)\), for either \(a=t\) or \(a=u\), lie strictly between
\(-1/4\) and \(3/4\). At nonnegative shifted real part the original
Gamma product is holomorphic and nonzero. At negative shifted
real part its reciprocal is continued by the exact identity
\[
 \frac1{G_N(Nw-1/2)}
   =\frac{2\cos(\pi Nw)}{N}\,G_N(-Nw-1/2).
\tag{4}
\]
The right side is holomorphic there; its cosine zeros introduce
no poles. The two continuations agree on their overlap.
Finally \(0<\Re(Ny)<N/2\), so the two own-factorial denominators
are nonzero. This proves (3), including the numerator-zero
locations that occur beyond the first quarter.

On each compact subset of (3), the sourcewise upper bound is
\[
 |T_N(y;t,u)|\le C N^{-2}
                e^{N\mathfrak F(y;t,u)},\qquad
 \mathfrak F(y;t,u)=\mathfrak b(y,t)+\mathfrak b(y,u).
\tag{5}
\]
The function \(\mathfrak b\) is the original sidewise real
factorial exponent from the uniform theorem, Section 3.
It is continuous through its zeros and negative-factorial
cuts. In the regular first quarter,
\(\mathfrak F=\Re F\) for the original holomorphic wire phase.
Elsewhere (5) is an upper bound with both reciprocal cosine
terms retained, not an asserted single relative expansion.

## 2. Physical endpoint groups and external caps

Write \(\psi(t,u)=F(y_*(u);t,u)\) for the original selected action.
The [first-quarter theorem](research_mixed_next_two_angle_bare_first_quarter_contour.md)
provides a fixed \(\alpha>0\) and a fixed positive gap on
the real interval \(0\le y\le2\alpha\), and pays all its
original physical rows.

The [right-end theorem](research_mixed_next_shortened_edge_endpoint_gap.md)
provides a fixed \(\delta>0\) such that the rows with
\(1/2-\delta\le j/N\le U/N\) have absolute sum at most
\(C e^{N(\Re\psi-1/50)}\). Its proof also gives a strict
real upper-exponent gap throughout the closed interval
\([1/2-\delta,1/2]\). Decrease \(\alpha\), if needed, and set
\[
                 \gamma=1/2-\delta/2,\qquad
 \alpha_N=\frac{\lfloor N\alpha\rfloor+1/2}{N},\qquad
 \gamma_N=\frac{\lceil N\gamma\rceil-1/2}{N}.
\tag{6}
\]
For all large \(N\),
\[
 0<\alpha_N<1/4<\gamma_N<U/N .
\]
Both cuts are original physical midpoints:
\(e^{2\pi iN\alpha_N}=e^{2\pi iN\gamma_N}=-1\).
The two removed physical groups are exactly
\[
 E_N^{\rm phys}=
 \sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N;t,u)
 +\sum_{j=\lceil N\gamma\rceil}^{U}T_N(j/N;t,u).
\tag{7}
\]
Their combined absolute sums are uniformly below the selected
rate by a fixed positive amount.

Uniform continuity in (5) now gives a fixed \(h_c>0\) and a
fixed \(\epsilon_c>0\) for which
\[
 \mathfrak F(x+iv;t(u),u)
       \le\Re\psi(t(u),u)-\epsilon_c,
 \quad x=\alpha_N\text{ or }\gamma_N,\quad |v|\le h_c,
 \quad u\in\mathcal U_+ .
\tag{8}
\]
The \(O(N^{-1})\) cut shifts are included by first choosing
small fixed real neighborhoods of \(\alpha,\gamma\).
This is a consequence of the already proved real endpoint
gaps, not a new estimate on an internal real cut.

Put \(\zeta_N(y)=e^{2\pi iNy}\), and orient each external
vertical segment upward. Define
\[
 C_N=N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
          \frac{T_N(y;t,u)}{\zeta_N(y)-1}\,dy
       -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
          \frac{T_N(y;t,u)}{\zeta_N(y)-1}\,dy .
\tag{9}
\]
At either midpoint, \(\zeta_N(x+iv)=-e^{-2\pi Nv}\), so
\[
                    |\zeta_N(x+iv)-1|^{-1}\le1 .
\tag{10}
\]
Equations (5),(8)--(10) pay each absolute vertical integral.
Thus, after absorbing fixed polynomial factors, for some
fixed \(\epsilon>0\),
\[
 |C_N|+|E_N^{\rm phys}|
        \le C e^{N(\Re\psi-\epsilon)} .
\tag{11}
\]
This includes both vertical halves and both physical endpoint
groups, at both parities.

## 3. An exact representation without the artificial middle side

Let \(\Gamma_+\) be any piecewise smooth path in
\(0<\Re y<1/2,\ \Im y>0\) from \(\alpha_N+ih_c\) to
\(\gamma_N+ih_c\). Let \(\Gamma_-\) be any such path in the
lower half-strip, from \(\alpha_N-ih_c\) to
\(\gamma_N-ih_c\). Both paths are oriented left to right.

**Theorem 1.** The original shortened kernel satisfies
\[
\boxed{\begin{split}
 K_N^{<}(t,u)
  ={}&N\int_{\Gamma_+}
             \frac{T_N(y;t,u)}{1-e^{2\pi iNy}}\,dy\\
     &+N\int_{\Gamma_-}
             \frac{T_N(y;t,u)}{e^{2\pi iNy}-1}\,dy
          +C_N+E_N^{\rm phys}.
\end{split}}
\tag{12}
\]
The last two terms have the uniform bound (11).
The formula is exact for every eligible finite level and every
stated path; the path integrals have not yet been estimated.

*Proof.* Begin with straight upper and lower horizontal paths.
The kernel \(1/(\zeta_N(y)-1)\) has residue \(1/(2\pi iN)\)
at every point \(j/N\). The positively oriented rectangle
therefore gives
\[
 N\oint \frac{T_N(y;t,u)}{\zeta_N(y)-1}\,dy
  =\sum_{j=\lfloor N\alpha\rfloor+1}^{\lceil N\gamma\rceil-1}
                    T_N(j/N;t,u).
\tag{13}
\]
The lower side is directed left to right and the upper side
right to left. Reversing the upper orientation changes its
denominator to \(1-\zeta_N\). The two remaining sides are
exactly (9). Add the physical groups (7) to obtain (12).

By (3), each path integrand is holomorphic in its respective
open half-strip. These half-strips are simply connected.
Cauchy's theorem therefore gives (12) for every stated
\(\Gamma_+\) and \(\Gamma_-\), with the same external caps.
No interpolation pole or physical residue is crossed.
\(\square\)

On a compact path at positive height \(v\), the first
reciprocal denominator in (12) is \(1+O(e^{-2\pi Nv})\). On a compact
path at negative height \(-v\), the second reciprocal denominator is
\(O(e^{-2\pi Nv})\). These are the exact sums of all the
original Fourier corrections. They must not be replaced
by unrelated finite sample bounds.

Equation (12) contains no vertical segment at any intermediate
real point \(\beta\). If it is derived by adjoining two
neighboring midpoint rectangles, their shared vertical
integrals cancel exactly, before absolute values are taken.
The [actual first-quarter obstruction](research_mixed_next_first_quarter_real_cut_obstruction.md)
shows why that cancellation is necessary: at \(u=0\), every
eligible separate real cut up to \(1/4\) has upper rate above
\(\Re\psi\).

## 4. The known Gaussian integral and the two remaining continuations

Retain the fixed \(\beta<1/4\) of the first-quarter theorem,
with \(\alpha<\Re y_*(u)<\beta\), and put
\[
 \beta_N=\frac{\lfloor N\beta\rfloor+1/2}{N},\qquad
                         h_*(u)=\Im y_*(u)>0 .
\tag{14}
\]
By compactness, decrease \(h_c\) so that
\(h_c<\frac12\min_{\mathcal U_+}h_*\).
Choose \(\Gamma_+\) to travel from \(\alpha_N+ih_c\)
vertically to \(\alpha_N+ih_*\), then horizontally to
\(\beta_N+ih_*\), and then along any upper-half-strip
continuation \(\Upsilon_+\) to \(\gamma_N+ih_c\).
Choose \(\Gamma_-\) by the corresponding left vertical
and reflected horizontal, followed by a lower-half-strip
continuation \(\Upsilon_-\) to \(\gamma_N-ih_c\).
No side descends from \(\beta_N+ih_*\) to the real axis.

Define the exact integral
\[
 I_N^{\rm edge}
     =N\int_{\alpha_N+ih_*}^{\beta_N+ih_*}T_N(y;t,u)\,dy.
\tag{15}
\]
The first-quarter theorem proves
\[
 I_N^{\rm edge}
   =N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
\]
\[
 a_e(t,u)=
 \frac{\sqrt{2\pi}}
  {4\sin^2(\pi y_*)\sqrt{-F_{yy}(y_*;t,u)}}\ne0 .
\tag{16}
\]
Its square root and normalization are the original ones.

**Corollary 2.** Uniformly on the actual positive outer family,
\[
\boxed{\begin{split}
 K_N^{<}(t(u),u)
   ={}& I_N^{\rm edge}
       +N\int_{\Upsilon_+}
          \frac{T_N(y;t(u),u)}{1-e^{2\pi iNy}}\,dy\\
      &+N\int_{\Upsilon_-}
          \frac{T_N(y;t(u),u)}{e^{2\pi iNy}-1}\,dy
        +O(e^{N(\Re\psi-\epsilon)})
\end{split}}
\tag{17}
\]
for some fixed \(\epsilon>0\). The error is the explicitly
removed source terms; it does not include the two continuation
integrals or the algebraic relative error inside (16).

*Proof.* On the first upper horizontal,
\(1/(1-\zeta_N)=1+\zeta_N/(1-\zeta_N)\).
The first term is (15); the second has the strict Fourier
penalty proved in the first-quarter theorem, equation (32).
On the reflected horizontal, the second denominator in (12)
gives precisely its lower Fourier penalty; equation (31)
of that theorem pays it uniformly.

The entire left upper joining segment is below the action:
vertical convexity reduces its upper profile to the already
paid real left cut and upper horizontal endpoint. On the
lower joining segment, the first-quarter reflected comparison
bounds the penalized lower profile by that same upper profile.
Both joins therefore retain a fixed gap. Their denominators
are uniformly controlled because their heights are at least
\(h_c>0\). Finally use (11) for the external caps and
physical endpoints. All prefactors are polynomial and are
absorbed by decreasing the positive gap. This proves (17).
\(\square\)

The unknown part in (17) is now a specified pair of original
integrals with no artificial internal real side. Their
initial upper endpoint lies on the descending side of the
known saddle contour; their terminal endpoints lie in the
already paid physical endpoint neighborhood. Establishing
a uniform bound for the full continuations is still necessary.
The upper continuation must retain the exact reciprocal
factorial behavior beyond the first quarter, and the lower
one must retain its full Fourier denominator.

No nonzero coefficient for the complete finite kernel follows
yet from (16). No negative outer-half statement, complete
inner-trace estimate, outer observation bound, arbitrary-short
filling stability, or finite-exceptions conclusion is asserted.

