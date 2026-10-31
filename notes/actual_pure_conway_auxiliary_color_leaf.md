# Exact auxiliary colors of the pure Conway leaf

29 October 2026. The literal turned crossing circle has an exact positive
core and a disjoint, signed alias at every ordinary auxiliary color.
Every alias coefficient is at most N/2 in absolute value, uniformly in
the color and at both parities. The complete-circle core also simplifies
to one positive factorial ratio. These are identities in the FULL pair
Casimir algebra, so they retain its projective normal directions.

The leaf here is `h_j=Rturn(L_j)`, the one used in the
[positive complete-circle Conway grammar](actual_positive_complete_circle_conway_trees.md).
It has no extra half-twist. The older belt leaf `Rturn(R^-1 L_j)` has a
different alias and is not covered by this bound. This local theorem
alone does not prove a global mixed-color gap or a long-filling theorem.

## 1. Literal source and notation

Set

\[
 q=e^{\pi i/N},\quad D=N-1,\quad M=\lfloor D/2\rfloor,
 \quad \theta=\pi/N,\quad
 s_r=\prod_{u=1}^r2\sin(u\theta),\quad s_0=1.
\]

Write \(\mathsf T_n(z)=2T_n(z/2)\), so
\(\mathsf T_0=2,\mathsf T_1=z\), and put

\[
 H_N=\mathbb C[z]/(\mathsf T_N(z)+2),\qquad
 c_k=q^{2k+1}+q^{-2k-1},\qquad
 B_r(z)=\prod_{k=0}^{r-1}(c_k-z),\qquad
 \widehat B_r=B_r/s_r^2.                                      \tag{1}
\]

The [original crossing-circle calculation](actual_crossing_circle_source_and_filling.md)
gives, for the actual auxiliary module of dimension j and its original
pivot, with no extra factor 1/j,

\[
 L_j=(-1)^{j-1}U_{j-1}(z/2),\quad 1\le j\le N,
 \qquad h_j=R_{\mathrm{turn}}L_j.                                 \tag{2}
\]

The [actual turn and marked closure](actual_positive_newton_multiplication.md)
satisfy

\[
 R_{\mathrm{turn}}\widehat B_r=\widehat B_{D-r},\qquad
 \phi(\widehat B_i\widehat B_j)=\delta_{i+j,D},\qquad
 \phi(L_Nf)=N\sum_{k=0}^{D}f(c_k).                           \tag{3}
\]

The sum counts each of the N listed roots, including repetitions.
These equations hold in the repeated-root algebra (1), not just its
quotient consisting of values at the distinct nodes. In particular
the \(\widehat B_v\) coefficient of \(R_{\mathrm{turn}}f\) is
\(\phi(f\widehat B_v)\).

## 2. A generic Chebyshev--Newton identity

With q initially generic and \({a\brack b}_q\) the symmetric quantum
binomial, one has the polynomial identity

\[
 U_{j-1}(z/2)=\sum_{r=0}^{j-1}(-1)^r
             {j+r\brack 2r+1}_q B_r(z).                     \tag{4}
\]

Here is a direct derivation. For a formal variable t, successive
division of \(1-zt+t^2=(1-c_rt+t^2)+t(c_r-z)\) gives

\[
 \frac1{1-zt+t^2}
   =\sum_{r\ge0}\frac{(-t)^rB_r(z)}
                         {\prod_{i=0}^{r}(1-c_it+t^2)}.     \tag{5}
\]

The remainder after r stages is divisible by \(t^{r+1}\), which
justifies the formal identity. The denominator in its rth term is

\[
 \prod_{a=0}^{2r+1}(1-q^{-(2r+1)+2a}t).
\]

Its reciprocal has coefficient of \(t^n\) equal to
\(q^{-(2r+1)n}{n+2r+1\brack 2r+1}_{q^2}\), where the binomial on
the right is the ordinary Gaussian one. This formula follows by
induction on the number of factors using the finite geometric series
and the Gaussian Pascal recurrence. Converting to the symmetric
binomial cancels the displayed q power. Taking \(n=j-r-1\) proves
(4), since the left side of (5) generates the Chebyshev polynomials.

For \(1\le j\le\lfloor N/2\rfloor\), all factorial arguments in
(4) are less than N. Specialization therefore gives, without any
zero-over-zero division,

\[
 \boxed{\quad h_j=
   \sum_{r=0}^{j-1}(-1)^{j-1+r}b_{j,r}\widehat B_{D-r},\qquad
 b_{j,r}=\frac{s_r^2s_{j+r}}{s_{2r+1}s_{j-r-1}}>0.\quad}      \tag{6}
\]

This is an equality of full polynomials of degree below N after the
actual turn, so it includes every repeated-node derivative. For larger
j one must retain the Laurent-polynomial binomial in (4), rather than
substitute a factorial quotient containing zeros. The next identity
avoids all such zero quotients.

## 3. Positive core plus the actual low-color alias

For \(0\le h\le M\), define \(L_0=h_0=0\). Then exactly

\[
 \boxed{\quad
 h_{N-h}=\sum_{v=h}^{M}A_{N,v}(h)\widehat B_v+(-1)^Nh_h,
 \qquad
 A_{N,v}(h)=\frac{N^2s_{2v}}
                  {s_v^2s_{v-h}s_{v+h}}>0.\quad}             \tag{7}
\]

The first sum is the core. If h>0, (6) puts the entire alias in
indices \(v\ge N-h\); these are disjoint from the core indices
\(h\le v\le M\). At h=0 the alias is zero. In particular the
complete-circle coefficients are simply

\[
 h_N=\sum_{v=0}^{M}a_{N,v}\widehat B_v,\qquad
 a_{N,v}=\frac{N^2s_{2v}}{s_v^4}.                            \tag{8}
\]

To prove (7), first use the elementary Chebyshev identity

\[
 U_{N-h-1}=\tfrac12(\mathsf T_hU_{N-1}
                              -\mathsf T_NU_{h-1}).
\]

It follows either by multiplying sines and cosines at
\(z=2\cos t\), then extending as a polynomial identity, or directly
from the Chebyshev recurrence. In the full algebra (1) it becomes

\[
 L_{N-h}=(-1)^h\frac{\mathsf T_h}{2}L_N+(-1)^NL_h.          \tag{9}
\]

No passage to root values was made in (9). To compute the turn of its
first term, it is now legitimate to use the special trace identity
(3). Its coefficient at v is

\[
 (-1)^hN\sum_{k=0}^{D}\cos(h(2k+1)\theta)
                             \widehat B_v(c_k).              \tag{10}
\]

For v>M, \(B_v\) vanishes at all the nodes c_k, so (10) is zero.
For v<=M, a finite Laurent expansion gives

\[
 B_v(w+w^{-1})=
    \sum_{u=-v}^{v}(-1)^u
           \frac{[2v]_q!}{[v+u]_q![v-u]_q!}\,w^u.           \tag{11}
\]

For example this follows from

\[
 B_v(w+w^{-1})
 =q^{-v^2}(qw;q^2)_v(q/w;q^2)_v
 =(-1)^vw^{-v}(q^{1-2v}w;q^2)_{2v},
\]

and the finite binomial expansion; its q powers cancel on conversion
to symmetric binomials. Evaluating at \(w=q^{2k+1}\), the Fourier
average in (10) selects u=+h and u=-h. There are no other Fourier
aliases because \(v+h\le2M<N\). The two equal terms cancel the
factor 1/2 in the cosine; at h=0 there is just its constant term.
This is exactly (7).

Moreover the core is pointwise dominated by the complete core:

\[
 0<A_{N,v}(h)\le a_{N,v}\quad(0\le h\le v\le M).           \tag{12}
\]

Indeed the ratio \(a_{N,v}/A_{N,v}(h)\) is
\(s_{v-h}s_{v+h}/s_v^2\). Its successive ratio as h increases is

\[
 \frac{\sin((v+h)\theta)}{\sin((v-h+1)\theta)}\ge1,
\]

since the two arguments sum to \((2v+1)\theta\le\pi\).
For h>0 this is strict except at the odd-level endpoint
\(v=(N-1)/2\), where equality holds for every allowed h.

## 4. An exact uniform N/2 bound for every alias coefficient

For all N>=2, \(1\le j\le\lfloor N/2\rfloor\), and \(0\le r<j\),

\[
 \boxed{\qquad 0<b_{j,r}\le N/2,\qquad
      \sum_{r=0}^{j-1}b_{j,r}\le jN/2\le N^2/4.\qquad}      \tag{13}
\]

The stronger final N^2/4 follows from j<=N/2. The proof uses the
actual sine product, not its limiting action. Rewrite (6) as

\[
 b_{j,r}=\frac{s_r^2}{s_{2r+1}}
             \prod_{u=-r}^{r}2\sin((j+u)\theta).             \tag{14}
\]

For fixed r this positive product, regarded as a function of real j
on \(r<j<N-r\), is symmetric about N/2 and log concave:
each summand \(\log\sin((j+u)\theta)\) has strictly negative
second derivative. Hence its maximum occurs at j=N/2. The value
of (14) there is

\[
 B_r=2\,
   \frac{\prod_{u=1}^{r}2\sin(2u\theta)}
        {\prod_{u=0}^{r}2\sin((2u+1)\theta)}.               \tag{15}
\]

Here one cancels \((2\sin u\theta)(2\cos u\theta)
=2\sin2u\theta\). The ratio

\[
 \frac{B_{r+1}}{B_r}
   =\frac{\sin((2r+2)\theta)}{\sin((2r+3)\theta)}
\]

is <=1 and then >=1, with at most one change: the comparison changes
at \((4r+5)\theta=\pi\). Thus the maximum over
\(0\le r\le\lfloor N/2\rfloor-1\) occurs at an endpoint.
At r=0 it is \(\csc\theta\). If N=2m, the other endpoint is
\(B_{m-1}=m\), because the even sine product in (15) is m and
the odd product is 2. These product evaluations follow directly by
factoring \(t^m-1\) and \(t^m+1\) at t=1. If N=2m+1, reflection
\(\sin(k\theta)=\sin((N-k)\theta)\) cancels the even factors
against the odd factors other than the first, and gives
\(B_{m-1}=\csc\theta\). Finally
\(\sin(\pi/N)\ge2/N\), proving (13).

Consequently the alias in (7) has a uniform polynomial coefficient
norm, even when its physical color h grows proportionally to N.
This is not a positive-source assertion: its coefficients genuinely
alternate. For odd N and h=1 the alias is
\(-\widehat B_D\). For even N>=4 and h=2, it has coefficient
\(-c_0\) at \(\widehat B_D\). These signs cannot be dropped in
the original mixed-color source.

## 5. Its real action and a marked local complex interpolation

Let \(J(x)=\int_0^x\log(2\sin\pi t)\,dt\). Uniformly at all
integer arguments between 0 and N-1, the elementary endpoint-aware
sum estimate is \(\log s_r=NJ(r/N)+O(\log N)\).
For a direct proof, subtract \(\log t+\log(1-t)\) from the
integrand. The remainder extends smoothly to [0,1] and has an O(1)
Riemann-sum error. The two subtracted logarithms give ordinary
factorial ratios, whose sum-minus-integral errors are O(log N)
uniformly, including r=0 and r=N-1.
Writing \(x=v/N\) and \(\chi=h/N\), (7) therefore has rate

\[
 \log A_{N,v}(h)=Ng_\chi(x)+O(\log N),\qquad
 g_\chi(x)=J(2x)-2J(x)-J(x-\chi)-J(x+\chi),                 \tag{16}
\]

uniformly over \(0\le h\le v\le M\). On the interior
\(0<\chi<x<1/2\),

\[
 \partial_\chi g_\chi(x)
   =\log\frac{\sin\pi(x-\chi)}{\sin\pi(x+\chi)}<0,
 \qquad
 \left.\partial_\chi^2g_\chi(x)\right|_{\chi=0}
   =-2\pi\cot(\pi x)<0.                                   \tag{17}
\]

The loss is uniform on compact interior sets with chi bounded away
from zero. At x=1/2 the continuum loss vanishes, consistently with
the exact odd-level endpoint equality in (12); an arbitrary global
color gap cannot be inferred without controlling endpoint sources.

There is also a fixed, even, holomorphic continuation of this actual
core coefficient, without assigning a formal Newton index the role
of a peripheral holonomy. Let G_N be the sine-factorial interpolation
proved in [the exact interpolation note](exact_factorial_interpolation_and_complex_contours.md),
with \(G_N(r)=s_r\), and define

\[
 \mathcal A_N(x,\chi)=
 \frac{N^2G_N(2Nx)}{G_N(Nx)^2G_N(N(x-\chi))G_N(N(x+\chi))}.
                                                                    \tag{18}
\]

It is holomorphic and nonzero wherever the four scaled arguments
lie in the interpolation's strip, and it agrees EXACTLY with (7)
at its lattice arguments. On any fixed compact complex corridor
where 2x, x, x-chi and x+chi have real parts strictly between 0 and 1,
the proved uniform factorial expansion gives

\[
 \mathcal A_N(x,\chi)
 =N^{1/2}\,
 \frac{\sqrt{\sin(2\pi x)}}
      {2^{3/2}\sin(\pi x)
       \sqrt{\sin\pi(x-\chi)\sin\pi(x+\chi)}}
 e^{Ng_\chi(x)}(1+O(N^{-1})).                              \tag{19}
\]

All logarithms and square roots are continued from the positive
real corridor. The error and every fixed derivative are uniform on
a smaller corridor. Thus the local coefficient is an even analytic
function of the ACTUAL auxiliary-color deficit chi, with the exact
finite values and their marks fixed. This does not assert that the
whole finite source already has a single analytic saddle packet:
its original support, alias pieces, boundary contributions and
contour still require their separate estimates.

## 6. Consequence for arbitrary fixed Conway circuits, and scope

There is a useful intrinsic description of the alias subspace:

\[
 \mathfrak n_N=\operatorname{span}\{\widehat B_v:
                   v\ge\lceil N/2\rceil\}
      =\operatorname{Nil}(H_N),\qquad \mathfrak n_N^2=0.     \tag{20}
\]

Indeed \(B_{\lceil N/2\rceil}\) contains every distinct factor
of \(\mathsf T_N+2\) once, including its simple factor at odd N.
The subspace on the left is therefore the kernel of evaluation at
all distinct nodes. Every remaining root has multiplicity two, so
this is precisely the square-zero nilradical. Equivalently the
exact Newton multiplication vanishes when its two input indices
sum to at least N. Formula (6) is triangular with nonzero last
coefficient \(b_{j,j-1}=s_{j-1}^2\), so

\[
 h_1,\ldots,h_{\lfloor N/2\rfloor}
       \quad\text{are a basis of }\mathfrak n_N.             \tag{21}
\]

Thus the signed alias is exactly part of the source's radical data.
In a product of any number of mixed pure leaves, terms with two
aliases vanish identically. In particular each robust three-leaf
seed contains at most one alias term in its exact expansion.
The actual turn reverses the Newton indices and does NOT preserve
this nilradical; it cannot be quotiented out of a Conway circuit.

Each ordinary circle color in an arbitrary fixed robust Conway
expression can now be replaced exactly by (6) or (7), followed by
the existing full Newton multiplication and actual coordinate
reversal for every turn. This gives a finite, source-preserving
signed circuit with polynomial alias leaf coefficients and positive
core coefficients bounded by the corresponding complete ones.
All original colors, marked cuts, pivots and normal directions are
retained. It is an exact deformation through ordinary AUXILIARY COLORS;
it is not yet a deformation in a separately identified geometric
meridian or longitude.

Polynomial leaf aliases can acquire exponential growth when
multiplied by other circuit factors. Consequently (13) alone is
not a proof of an exponentially negligible whole alias sector.
That global source comparison, the complex whole-source saddle,
and the geometric peripheral interpretation are the additional
steps needed before invoking a long-filling transfer theorem.

Audit: [generic polynomial identities, all root coefficients and literal physical turns](../experiments/audit_actual_pure_conway_auxiliary_color_leaf.py).
The principal-root inequalities are proved above; finite-field
calculations are used only to verify exact identities.
