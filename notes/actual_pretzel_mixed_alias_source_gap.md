# A uniform original-source alias gap near complete pretzel colors

29 October 2026. For every fixed odd number of boxes \(s\geq5\),
the high-band terms in the exact cusp-color split are exponentially
smaller than the complete augmented geometric period on a sufficiently
small, fixed cusp-color corridor. This is a bound on the original
source, including all Casimir normal coefficients. The complete-color
circle estimate is used coherently before passing to its Hermite norm.

The assertion is an error bound relative to the **complete-color**
geometric rate. To obtain a mixed-color asymptotic one must still prove
the selected core asymptotic, with a comparable rate, throughout that
corridor. No fixed-filling volume theorem follows here. For \(s=3\)
the proof below has zero limiting margin; a separate cancellation is
needed.

Use \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(x=q^d=-q^{-1}\), and \(M=\lfloor d/2\rfloor\). All boxes,
turns and the source \(\Phi _2\) are exactly those in
[the original complete-base polynomial theorem](actual_pretzel_complete_base_casimir_polynomial.md).
The exact two-band split is

\[
 z_{N,r}=c_{N,r}+R P_{N,r},\qquad 0\leq r\leq M,
 \qquad \|RP_{N,r}\|_{\mathrm H}\leq56^r\quad(r>0),
 \tag{1}
\]

where \(r=N-j\) is the actual auxiliary-color deficit and the
remainder is zero for \(r=0\). The faithful norm and all source
normalizations are retained from
[the two-band theorem](actual_pretzel_cusp_color_two_band_bound.md).

## 1. A bounded dual Casimir on a coherent circle

Let \(\mathscr R\) be the literal quarter-turn, and define
\(\mathcal D=\mathscr R\circ(\Omega\cdot)\circ\mathscr R^{-1}\)
on the physical pair commutant. In the physical continuant basis,

\[
 \boxed{\quad \mathcal D f_v=c_v f_v+b_v f_{v-1},\qquad
 c_v=q^{2v+1}+q^{-2v-1},\quad b_v=Q^v+Q^{-v}-2.\quad}
 \tag{2}
\]

Here \(b_0=0\). This operator preserves polynomial degree, including
in the full degree-\(d\) algebra, so it preserves the low core.

For completeness, (2) follows from an actual Hopf Ward identity.
For a pair intertwiner \(B\), write
\(\beta_v=B_{d,v;d,v}\). The original coproduct of \(F\) gives

\[
 B_{d-1,v+1;d,v}=
 x^{-1}Q^d\frac{1-Q^{v+1}}{1-Q^d}
                       (\beta_{v+1}-\beta_v).
 \tag{3}
\]

The last row of the physical \(\Omega\) block of total degree
\(d+v\) has off-diagonal
\(Q^{-1}(1-Q)(1-Q^{-v-1})\) and diagonal
\(2q^{-1}+(q-q^{-1})Q^{-v-1}\). Inserting (3) gives

\[
 (\Omega B)_{d,v;d,v}
 =c_v\beta_v+
 q^{-1}(1-Q^{v+1})(1-Q^{-v-1})\beta_{v+1}.
\]

The first row of the rotated box is
\(x^{v-d}\beta_v\); its adjacent phase converts the second
coefficient to \(b_{v+1}\). The cyclic first row of the middle
Casimir block proves (2) for the entire commutant, not just its
semisimple quotient.

In the symmetric Laurent variable \(z=w+w^{-1}\), (2) is the
explicit rational difference operator

\[
 (\mathcal D F)(w)=a(w)F(Qw)+a(w^{-1})F(Q^{-1}w)+c(w)F(w),
 \tag{4}
\]
\[
 a(w)=\frac{(qw-1)^3}{q(w^2-1)(qw+1)},\qquad
 a(w^{-1})=\frac{(w-q)^3}{q(w+q)(w^2-1)},\qquad
 c(w)=\frac{8qw}{(w+q)(qw+1)}.
\]

Here \(F(w)\) means \(f(w+w^{-1})\). This formula is exact at
the specified root and retains every normal coefficient. Its apparent
poles are removable on symmetric Laurent polynomials.

An all-degree algebra check of (4) is short. Put
\(P_r(w)=(qw;Q)_r(q/w;Q)_r\). The two shifted product ratios give

\[
 \mathcal D P_r=c_rP_r-
                  \frac{(Q^r-1)^4}{qQ^r}P_{r-1}.
 \tag{5}
\]

Expand the physical continuant by its finite identity

\[
 f_v=x^v\sum_{r=0}^v
       \frac{(Q^{-v};Q)_rQ^r}{F_r^3}P_r.
\]

The ratios of adjacent coefficients are
\((1-Q^{r-v})Q/(1-Q^{r+1})^3\) and
\(x^{-1}(1-Q^{r-v})/(1-Q^{-v})\). Substitution in (5) proves
(2) coefficient by coefficient. All denominators \(F_r\) here have
\(r<N\); no root-zero division or omitted self-pair is used.

For every fixed radius \(\varrho>1\), let
\(\|f\|_{\varrho}=\max_{|w|=\varrho}|f(w+w^{-1})|\).
Since \(|Q|=1\), the shifts preserve that circle, and (4) gives

\[
 \boxed{\quad \|\mathcal D f\|_{\varrho}
       \leq K_{\varrho}\|f\|_{\varrho},\qquad
 K_{\varrho}=2+\frac{16\varrho}{(\varrho-1)^2}.\quad}
 \tag{6}
\]

Indeed each shifted coefficient is at most
\((\varrho+1)^2/(\varrho-1)^2\), and the central one at most
\(8\varrho/(\varrho-1)^2\). The constant is independent of
\(N\), polynomial degree and color deficit.

## 2. All low cores are generated from the complete core

Let \(\mathsf T_r(z)=2\cos(r\arccos(z/2))\), including
\(\mathsf T_0=2\). The elementary sine addition identity, reduced
modulo the FULL \(\mathcal P_N=\mathsf T_N+2\), gives

\[
 L_{N-r}=(-1)^N L_r+
                 \frac{(-1)^r}{2}\mathsf T_r(\Omega)L_N.
 \tag{7}
\]

Multiply by the literal half twist \(R^{-1}\), then rotate.
For \(1\leq r\leq M\), the rotated \(R^{-1}L_r\) has only
the high continuant band \(v\geq N-r>M\); this is the same finite
Gaussian support computation used in the two-band theorem.
The second term of (7) has degree at most \(M\) after rotation,
by (2). Consequently the low-degree projection is exactly

\[
 \boxed{\quad c_{N,r}=\frac{(-1)^r}{2}
                         \mathsf T_r(\mathcal D)z_N.\quad}
 \tag{8}
\]

The Chebyshev recurrence and (6) imply, also for \(r=0\),

\[
 \|c_{N,r}\|_{\varrho}
       \leq (K_{\varrho}+1)^r\|z_N\|_{\varrho}.
 \tag{9}
\]

This keeps the coherent complete-base polynomial. Bounding its
continuant summands separately is unnecessary.

The interval \([-2,2]\) lies inside the ellipse
\(w+w^{-1}\), \(|w|=\varrho\). By the maximum principle and
the ordinary degree-\(M\) Markov inequality, applied to a real
part after a unit phase rotation at each derivative evaluation,

\[
 \|c_{N,r}\|_{\mathrm H}
 \leq(1+M^2/N^2)\|c_{N,r}\|_{\varrho}
 \leq\frac54(K_{\varrho}+1)^r\|z_N\|_{\varrho}.
 \tag{10}
\]

Thus the passage to the faithful normal-source norm costs only a
constant. It does not drop the source derivative.

## 3. A strict source alias gap for every odd \(s\geq5\)

The proved coherent-circle theorem in
[the complete-base asymptotic](actual_pretzel_coherent_circle_and_period_asymptotic.md)
gives, for each fixed \(\eta>0\),

\[
 \limsup_{N\to\infty}\frac1N
           \log\|z_N\|_{e^\eta}\leq j(\eta),\qquad
 j(0)=\frac{v_8}{\pi},\qquad
 j'(\eta)=\frac1\pi\arctan\sinh(\eta/2).
 \tag{11}
\]

In particular \(j(\eta)-j(0)=O(\eta^2)\). Uniformly over every
integer color choice \(0\leq r_i\leq\delta N\), a source term
with a nonempty alias set \(S\), \(|S|=m\), has upper rate

\[
 \frac1N\log\left|\Phi_2\left(
       \prod_{i\in S}RP_{N,r_i}
       \prod_{i\notin S}c_{N,r_i}\right)\right|
 \leq (s-m)j(\eta)
 +\delta\big[(s-m)\log(K_{e^\eta}+1)+m\log56\big]+o(1).
 \tag{12}
\]

The \(o(1)\) is uniform in these colors. This is (1), (10),
submultiplicativity of the faithful norm, and the exact estimate
\(|\Phi_2(f)|\leq3N^3\|f\|_{\mathrm H}\).
The finite sum of at most \(2^s-1\) such terms has the same upper
rate. All original circle, half-twist and source phases remain in
the exact terms being bounded.

Let

\[
 A_s=\frac{V_s}{2\pi}
 =\frac{4s}{\pi}
   \left[\Lambda\left(\frac\pi4+\frac\pi{2s}\right)
         +\Lambda\left(\frac\pi4-\frac\pi{2s}\right)\right].
\]

The complete-base theorem proves the original source has rate
\(A_s\). Its margin over the worst alias envelope at \(\delta=0\)
is

\[
 g_s=A_s-(s-1)j(0)>0\qquad(s\geq5).
 \tag{13}
\]

Here is an elementary uniform proof. With
\(A(\alpha)=\Lambda(\pi/4+\alpha/2)+
\Lambda(\pi/4-\alpha/2)\),
\(A(0)=G\) (Catalan's constant), \(A'(0)=0\), and
\(A''(\alpha)=-1/(2\cos\alpha)\). Hence

\[
 g_s\geq\frac{4G}{\pi}-
                       \frac{\pi}{s\cos(\pi/s)}>0
                       \qquad(s\geq5).
\]

Indeed the second summand is less than 1 for \(s\geq5\), while
\(4G/\pi>1\), for example from \(G>1-1/9\).

Fix \(\eta>0\) with
\((s-1)(j(\eta)-j(0))<g_s/4\), and then fix
\(\delta>0\) so that
\(s\delta[\log(K_{e^\eta}+1)+\log56]<g_s/4\),
and also \(\delta<1/4\).
Equations (12)--(13) prove the genuine uniform original-source bound

\[
 \boxed{\quad
 \left|\Phi_2\left(\prod_i z_{N,r_i}
                         -\prod_i c_{N,r_i}\right)\right|
 \leq \exp\{N(A_s-g_s/2+o(1))\},
 \quad 0\leq r_i\leq\delta N,
 \quad s\geq5\text{ odd}.\quad}
 \tag{14}
\]

One may choose \(\eta\) of order \(\sqrt\delta\) as
\(\delta\downarrow0\); (12) then loses
\(O_s(\delta\log(1/\delta))\) above \((s-1)j(0)\).
This optimization is not needed for the fixed-corridor theorem.

The proof does not estimate the low-core **selected period** from
below, does not supply a gap for all colors outside the corridor,
and does not sum the filling kernels. Those are separate questions.

## 4. The other color-cube corners are also controlled

For an actual small ordinary color \(1\leq j\leq M\), the same
finite Gaussian support computation gives a pure high band. Exact
sine-factorial complementation gives the particularly simple identity

\[
 \boxed{\qquad z_{N,N-j}=(-1)^N R P_{N,j},\qquad
            \|z_{N,N-j}\|_{\mathrm H}\leq56^j.\qquad}
 \tag{15}
\]

For example \(j=1\) is exactly the original crossing \(R\).
To see that the uniform constant does not acquire an extra
\(N^{O(j)}\) factor, the apparent upper-band ratio is

\[
 \frac{s_{N-j+t-1}}{s_{2t-1}s_{N-j-t}}
       =\frac{s_{j+t-1}}{s_{2t-1}s_{j-t}},\qquad1\leq t\leq j.
\]

It is the SAME short Gaussian ratio as in the \(56^j\) proof.
All large factorial indices are complemented before estimating.

Consequently let every actual color \(j_i\) lie either in the low
corner \(1\leq j_i\leq\delta N\) or the complete corner
\(N-\delta N\leq j_i\leq N\). If at least one color is in the
low corner, expand only the complete-corner colors by (1).
Every resulting term has at least one short crossing sector.
The proof of (14) therefore gives uniformly

\[
 \left|\Phi_2\left(\prod_i z_{N,N-j_i}\right)\right|
 \leq\exp\{N(A_s-g_s/2+o(1))\},\qquad s\geq5\text{ odd}.
 \tag{16}
\]

Thus all the OTHER binary corners of the original color cube have
a rigorous gap. This does not cover its intermediate-color slabs.

## 5. The three-box endpoint is genuinely source-sensitive

For \(s=3\), \(A_3=2j(0)\), so (13) has zero margin.
The full source \(\Phi_2(Rz_N^2)\) is a useful diagnostic: its
nodal maximum has rate approaching \(2j(0)\), but direct evaluation
of the complete derivative-plus-value source at levels
\(N=16,32,64,128\) gives respectively

\[
 N^{-1}\log|\Phi_2(Rz_N^2)|=
 1.2930259621,\ 1.2612009276,\ 1.2297272136,\ 1.2060473620.
\]

These finite values suggest an additional source cancellation.
They neither prove its rate nor justify a uniform mixed-color gap.
The accompanying audit retains the exact crossing derivative in
this diagnostic and replays the high-level value at doubled precision.

## 6. The global intermediate-color test remains a diagnostic

[The separate exact-source diagnostic](../experiments/diagnose_actual_pretzel_global_colored_source.py)
evaluates all equal-color and all single-changed-color periods at
\(N=24,48,72\), \(s=3,5\), using the literal all-color two-band
coefficients and the complete derivative-plus-value functional.
It also checks 544 sorted mixed-color samples at \(N=48\), and
replays the selected source values at doubled precision. The sampled
maximum is complete color; the largest noncomplete sampled tuples
are \((0,0,4)\) and \((0,0,0,0,4)\) in color deficits.
This supplies no uniform asymptotic upper bound for intermediate
colors or for the unsampled mixed-color cube. In particular it is
not an input to (14) or (16).
