# Exact torus composition of the conditional three/four transfers

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

After one index family has been summed coherently, the remaining
cyclic source, and each open source with complete ordinary boundary
jets, has a global Laurent-polynomial representation. It
admits contour deformation on arbitrary nonzero circle radii with
every outer Fourier alias explicit: none at a three-type variable,
and one at a four-type variable. This is an exact composition
identity, not a claim that an alias or a remaining complementary
cycle is small.

## 1. A common polynomial kernel and exact diagonal cancellation

Let \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\[
 p_j(X)=(rX;r)_j,\qquad
 C_{\epsilon,N}(X,Y)=
   \sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)p_j(Y)}
                              {P_j^{2+\epsilon}},
          \quad\epsilon\in\{0,1\}.
 \tag{1}
\]
These are single global Laurent polynomials on
\((\mathbb C^\times)^2\). Their separate Fourier bands are
\[
       \deg_X C_{\epsilon,N}\subset[-N+1,0],\qquad
       \deg_Y C_{\epsilon,N}\subset[0,N-1].
 \tag{2}
\]
At the physical nodes \(X=r^a,Y=r^b\), the
[original conditional identities](research_mixed_conditional_leg_sum.md)
give exactly
\[
 L_\epsilon(a,b)=P_aP_b\,C_{\epsilon,N}(r^a,r^b),\qquad
 T_\epsilon(a,b)=\frac{P_b^{1-\epsilon}}{P_a}
                           C_{\epsilon,N}(r^a,r^b).
 \tag{3}
\]
The factors past the physical support vanish in \(p_j(r^a)\)
or \(p_j(r^b)\); (3) retains every original summand.

Indeed \(P_{j+a}=P_a p_j(r^a)\) on the surviving support,
and the polynomial on the right is zero when \(j+a\ge N\).
The original chirp is \(r^{-aj}=X^{-j}\), giving (1)--(3).
For nonphysical complex neighbors, the canonical fixed-sum
continuation is exactly
\[
 \mathcal L_{\epsilon,N}(\alpha,\beta)
   =\widehat P_N(N\alpha)\widehat P_N(N\beta)
      C_{\epsilon,N}(e^{-2\pi i\alpha},e^{-2\pi i\beta}).
 \tag{4}
\]
This is a definition by the same finite products, not an identification
with every possible interpolation through the physical grid.
For \(\epsilon=1\), it is the
[proved canonical continuation](research_mixed_four_conditional_complex_neighbors.md).

Let a cyclic word have \(m\ge1\) letters \(3+\epsilon_v\),
with \(k=\sum_v\epsilon_v\), and use cyclic subscripts.
The diagonal factors in (3) cancel exactly:
\[
 \begin{split}
 \operatorname{tr}(A_{3+\epsilon_1}\cdots A_{3+\epsilon_m})
 =\kappa^{m+k}N^k
   \sum_{a_1,\ldots,a_m=0}^{N-1}
     \prod_{v=1}^m
       C_{\epsilon_v,N}(r^{a_v},r^{a_{v+1}})
                              P_{a_{v+1}}^{-\epsilon_v}.
 \end{split}
 \tag{5}
\]
Here \(A_n=JM^n\) and \(\kappa\) are the original finite matrices
and scalar. Equation (5) follows from their exact conditional
trace formula. It includes both parities and the original
repeated-root normal data, rather than a semisimple quotient.

## 2. The exact diagonal weight and its forced transport

Define the unique polynomial of degree less than \(N\) with
values \(d_N(r^a)=1/P_a\):
\[
 \begin{split}
 d_N(X)&=\frac1N\sum_{q=0}^{N-1}e_{-q}X^q,\qquad
      e_q=\sum_{a=0}^{N-1}\frac{r^{qa}}{P_a},\\
 &=\frac{1-X^N}{N}
      \sum_{a=0}^{N-1}\frac{1}{P_a(1-Xr^{-a})}.
 \end{split}
 \tag{6}
\]
The apparent poles in the second line are removable. Its values
at a root of unity follow by a finite geometric sum, proving
both the interpolation and its uniqueness.

The original forced moment recurrence is
\(e_{q+1}=(1-r^q)e_q+1/N\). In particular \(e_1=1/N\);
the highest coefficient of \(d_N\) is exactly
\[
                            [X^{N-1}]d_N=\frac1{N^2}.
 \tag{7}
\]
Coefficient comparison gives the polynomial identity
\[
 (1-rX)d_N(rX)-d_N(X)
       =-\frac1{N^2}\sum_{q=1}^{N}(rX)^q.
 \tag{8}
\]
Equivalently,
\[
 d_N(r^{-1}X)
    =(1-X)d_N(X)+\frac{X(1-X^N)}{N^2(1-X)}.
 \tag{9}
\]
The quotient has its removable value \(N\) at \(X=1\).
These equations keep the actual finite forcing. A homogeneous
inverse-factorial solution cannot be substituted for \(d_N\)
without estimating their difference in the required complex domain.

## 3. Exact composition on arbitrary circle radii

**Theorem 1.** For arbitrary radii \(\rho_1,\ldots,\rho_m>0\),
the entire original cyclic source equals
\[
 \begin{split}
 &\operatorname{tr}(A_{3+\epsilon_1}\cdots A_{3+\epsilon_m})\\
 &\quad=\kappa^{m+k}N^{m+k}
 \oint_{|X_1|=\rho_1}\!\cdots\!
 \oint_{|X_m|=\rho_m}
 \prod_{v=1}^m
 \left[
 C_{\epsilon_v,N}(X_v,X_{v+1})
 \{d_N(X_{v+1})(1+X_{v+1}^{-N})\}^{\epsilon_v}
 \right]
                   \prod_{v=1}^m\frac{dX_v}{2\pi iX_v}.
 \end{split}
 \tag{10}
\]
All circles are counterclockwise. There is exactly one explicit
additional alias at each variable carrying a type-four diagonal
weight, and none at the other variables. The formula also holds
for \(m=1\), when the two arguments of a kernel coincide.

*Proof.* In (5), replace each \(P_a^{-1}\) by \(d_N(r^a)\),
which is exact. A variable \(X_v\) occurs as the right argument
of the previous kernel and the left argument of the next kernel.
By (2), before multiplication by its possible \(d_N\), its
Fourier band is contained in \([-N+1,N-1]\).
Without that weight, the only multiple of \(N\) is zero.
With it, the band is contained in \([-N+1,2N-2]\), whose only
multiples of \(N\) are zero and \(N\). Root averaging thus
selects exactly the constant term of the same function multiplied
by \(1+X_v^{-N}\) in the latter case.

Doing this in every variable proves (10); the \(m\) root
averages contribute \(N^m\). A Laurent polynomial has no poles
away from zero, so its constant term is independent of all
positive circle radii. This also proves exact simultaneous or
sequential radial deformation. No seam current, physical
endpoint or additional Fourier alias is omitted. \(\square\)

One may instead write the weighted factor as
\[
 d_N(X)(1+X^{-N})=\{X^{-N}d_N(X)\}(1+X^N).
 \tag{11}
\]
The latter places the interpolated weight in negative degrees.
It is the same exact integrand, not permission to discard either
of its two terms on a selected contour.
For \(X=e^{-2\pi iz}\), the wrapped term is \(X^{-N}=e^{2\pi iNz}\).
It grows when \(\Im z<0\) and changes the corresponding phase by
\(2\pi iz\). A local approximation to \(d_N\) does not remove this
additional phase.

## 4. Positive three-kernel, weighted four-kernel and the wrapped part

For \(|X|=1\), let
\(\tau_j=(-1)^j r^{j(j+1)/2}\), so that \(P_j^2=\tau_j S_j^2\).
The self-reciprocity of the finite product gives
\(X^{-j}p_j(X)=\tau_j\overline{p_j(X)}\). Therefore on the
unit circle in both variables,
\[
 C_{0,N}(X,Y)=\sum_{j<N}
       \frac{\overline{p_j(X)}p_j(Y)}{S_j^2},\qquad
 C_{1,N}(X,Y)=\sum_{j<N}
       \frac{\overline{p_j(X)}p_j(Y)}{S_j^2P_j}.
 \tag{12}
\]
The first is a positive Hermitian Gram kernel. The second retains
the complex original weight. This does not supply a simultaneous
positive metric for the two original transfers.

The outer alias has a particularly explicit interpretation.
Let \(f,g\) be analytic polynomials of degree less than \(N\).
The exact weighted root observation is
\[
 \frac1N\sum_{a=0}^{N-1}
       \frac{\overline{f(r^a)}g(r^a)}{P_a}
   =\oint_{|X|=1}\overline{f(X)}g(X)
             d_N(X)(1+X^{-N})\,\frac{dX}{2\pi iX}.
 \tag{13}
\]
Write \(d_N(X)=\sum_{q=0}^{N-1}d_qX^q\). In the monomial
basis \(1,X,\ldots,X^{N-1}\), the first integral on the right
has lower-triangular Toeplitz matrix \(d_{a-b}\), with entries
zero when \(a<b\). The additional alias has matrix
\[
 E_{ab}=
 \begin{cases}
 d_{N+a-b},&b>a,\\
 0,&b\le a.
 \end{cases}
 \tag{14}
\]
Their sum is the original cyclic Fourier matrix
\(e_{b-a}/N\). In particular
\[
 E^N=0,\qquad
 (E^{N-1})_{0,N-1}=N^{-2(N-1)},\qquad
                         \operatorname{rank}E=N-1.
 \tag{15}
\]
Indeed every first-superdiagonal entry is \(d_{N-1}=1/N^2\).
Thus the finite forcing determines a full nilpotent wrapped
operator. A rank-one forcing term in a recurrence is not a
rank-one bound for the Fourier alias. Nilpotence supplies no
small norm estimate after a change of basis.

## 5. Open words with the original complete boundary jets

Put \(q=e^{\pi i/N}\), so \(r=q^{-2}\), and retain the original
Newton evaluation vector \(v(w)\). For every integer \(a\ge0\), let
\(E_{\ell,a}=(-1)^a e_\ell^{(a)}(-2)\) and define
\[
 \begin{split}
 H_{N,a}(Y)&=\sum_{\ell=0}^{N-1}
       \frac{(-q)^{-\ell}E_{\ell,a}}{P_\ell}(Y;r)_\ell,\\
 b_j^{(a)}(-2)&=(-1)^a\,\frac{H_{N,a}(r^{-j})}{P_j}.
 \end{split}
 \tag{16}
\]
The second identity is the exact polynomial form of the
[original complete-boundary coefficient](research_complete_boundary_complex_index.md#6-its-finite-polynomial-and-exact-difference-equation).
It includes the odd simple endpoint and all repeated-root normals.
In particular \(\deg H_{N,a}<N\), without division by a possibly
zero complete Newton value.

For \(\epsilon=0,1\), define the polynomial
\[
 \begin{split}
 U_{\epsilon,a,N}(X)
   &=\sum_{i=0}^{N-1}
       \frac{H_{N,a}(r^{-i})p_i(X)}{P_i^{1+\epsilon}},\\
 \sum_{i<N}b_i^{(a)}(-2)
       \frac{(B_{3+\epsilon})_{ij}}{\kappa^{1+\epsilon}N^\epsilon}
   &=(-1)^aP_j^{1-\epsilon}U_{\epsilon,a,N}(r^j).
 \end{split}
 \tag{17}
\]
Here \(\deg U_{\epsilon,a,N}<N\). The second line follows by
substituting \(B_{3+\epsilon,ij}/(\kappa^{1+\epsilon}N^\epsilon)
=P_{i+j}/(P_iP_j)^\epsilon\), with its exact zero when \(i+j\ge N\).
The polynomial \(p_i(r^j)\) retains precisely that support.
For every later vertex the exact contraction gives
\[
 \sum_{i<N}\Gamma_{h i}
       \frac{(B_{3+\epsilon})_{ij}}{\kappa^{1+\epsilon}N^\epsilon}
       =\frac{P_j^{1-\epsilon}}{P_h}
                       C_{\epsilon,N}(r^h,r^j).
 \tag{18}
\]
Indeed the left summand is
\(r^{-hi}P_{h+i}P_{i+j}/(P_h^2P_i^{2+\epsilon}P_j^\epsilon)\);
substitution of the two finite products proves (18), including
both support zeros.

Let \(\mathcal Z_N^{a,b}\) denote
\(\partial_{w_L}^a\partial_{w_R}^b
 [v(w_L)^TA_{3+\epsilon_1}\cdots A_{3+\epsilon_m}v(w_R)]\)
at \(w_L=w_R=-2\). Equations (16)--(18) telescope all diagonal
factors to give
\[
 \begin{split}
 \mathcal Z_N^{a,b}
  ={}&(-1)^{a+b}\kappa^{m+k}N^k
    \sum_{j_1,\ldots,j_m=0}^{N-1}
       U_{\epsilon_1,a,N}(X_1)
       \prod_{v=2}^m C_{\epsilon_v,N}(X_{v-1},X_v)\\
  &\hspace{30mm}\times H_{N,b}(X_m^{-1})
                         \prod_{v=1}^m P_{j_v}^{-\epsilon_v},
       \qquad X_v=r^{j_v}.
 \end{split}
 \tag{19}
\]
This uses the full exact open-word contraction with \(m-1\) shared
Gram matrices. No cyclic trace or extra shared boundary is inserted.

**Theorem 2.** For every word of length \(m\ge1\), every ordinary
derivative order \(a,b\ge0\), both level parities, and arbitrary
positive circle radii,
\[
 \begin{split}
 \mathcal Z_N^{a,b}
  ={}&(-1)^{a+b}\kappa^{m+k}N^{m+k}
    \oint\cdots\oint
       U_{\epsilon_1,a,N}(X_1)
       \prod_{v=2}^m C_{\epsilon_v,N}(X_{v-1},X_v)\\
  &\hspace{10mm}\times H_{N,b}(X_m^{-1})
       \prod_{v=1}^m
          \{d_N(X_v)(1+X_v^{-N})\}^{\epsilon_v}
                       \prod_{v=1}^m\frac{dX_v}{2\pi iX_v}.
 \end{split}
 \tag{20}
\]
The circles are counterclockwise. In this open indexing the
four-weighted variable is \(X_v\) when \(\epsilon_v=1\).

*Proof.* The first variable has a nonnegative degree-\((N-1)\)
factor \(U\) and a nonpositive degree-\((N-1)\) factor from the
next kernel. The last has a nonnegative factor from the preceding
kernel and the nonpositive factor \(H(X_m^{-1})\). The internal
variables have the bands used in Theorem 1. When \(m=1\), the
two factors are simply \(U(X_1)\) and \(H(X_1^{-1})\).
Thus every unweighted variable has band
\([-N+1,N-1]\), in all cases. Multiplication by \(d_N\) introduces
exactly the same single possible \(+N\) alias as before. Apply
root averaging to (19), one variable at a time. This proves
(20), its scalar \(N^{m+k}\), and invariance under all positive
radial deformations. All sums and derivatives are finite, so the
same proof applies to every indicated original ordinary jet.
\(\square\)

No asymptotic for the new polynomial \(U_{\epsilon,a,N}\) is
asserted. The open identity is an exact source representation;
it does not supply boundary-packet dominance or a knot theorem.

**Corollary 3 (the whole boundary polynomial).** Define
\[
 \begin{split}
 \mathcal H_N(w,Y)
    &=\sum_{\ell=0}^{N-1}
       \frac{(-q)^{-\ell}e_\ell(w)}{P_\ell}(Y;r)_\ell,\\
 \mathcal U_{\epsilon,N}(w,X)
    &=\sum_{i=0}^{N-1}
       \frac{\mathcal H_N(w,r^{-i})p_i(X)}{P_i^{1+\epsilon}}.
 \end{split}
 \tag{21}
\]
For arbitrary complex \(w_L,w_R\), formula (20), with its sign
\((-1)^{a+b}\) removed and its endpoint factors replaced by
\(\mathcal U_{\epsilon_1,N}(w_L,X_1)\) and
\(\mathcal H_N(w_R,X_m^{-1})\), equals the entire original polynomial
\(v(w_L)^TA_{3+\epsilon_1}\cdots A_{3+\epsilon_m}v(w_R)\).
All circles and all aliases are unchanged.

Indeed the same direct finite algebra applies to \(b(w)=Sv(w)\).
Alternatively,
\(\partial_w^a\mathcal H_N(-2,Y)=(-1)^aH_{N,a}(Y)\), and the
same relation holds for \(\mathcal U\). Theorem 2 therefore matches
every Taylor coefficient of the two polynomials at \((-2,-2)\);
their degrees are at most \(N-1\) in each boundary color.
This exact identity makes no uniform free-color asymptotic assertion.

## 6. What this permits and what is still needed

Theorem 1 replaces the remaining physical root sums by one exact
global torus integral with explicit polynomial weights. It makes
outer contour deformation legal without appealing to an
unspecified off-grid continuation of a varying conditional cutoff.
The canonical finite functions in (4) control the corresponding
kernel factors wherever their proved packets apply.

The [reciprocal-factorial comparison](research_mixed_fourier_weight_continuation.md)
now estimates \(d_N\) with exponentially small relative error on the
rectangle containing all type-four critical disks, while retaining
the forced transport (8)--(9). That is a local estimate for one
factor. All terms in (10), including the explicit aliases, must
still be controlled on the required full contours before making a
statement about the remaining observed coefficient. Positivity of (12) alone does
not give that lower bound, and taking absolute values of the
whole remaining sum still loses its oscillation.

Theorem 2 and Corollary 3 supply the corresponding exact bookkeeping
for the whole ordinary boundary polynomials of open words, including
every ordinary jet. Their endpoint polynomials and all wrapped terms
remain in the integral. A complex free-color asymptotic or a
nonzero closing coefficient does not follow from this algebra.
No knot interpretation of an arbitrary matrix cycle is asserted.

## 7. Reproduction

Reproduce the finite algebra checks with:

    python3 experiments/check_mixed_conditional_torus_composition.py

The checker uses exact arithmetic at levels \(2,3,4,6\).
It checks the original normalized word traces, diagonal
cancellation, interpolation and its forcing, all allowed
monomial quadratures, and the full wrapped operator. The
open-source checks compare both root sums and full torus
quadrature with the literal original matrices at ordinary
derivative orders \(0,1,2\) at each boundary. The all-level
statements follow from the finite identities above.
