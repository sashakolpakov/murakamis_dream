# Two limitations of absolute bounds on the left region

Research note, 4 November 2026. These are obstructions to two proposed
pointwise estimates, not to the original cyclic integral or its volume
asymptotic. Completed source and contour theorems are unchanged.

Put
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)+2\pi ias,
 \qquad
 \phi(a,b)=Q(s_*(a,b);a,b)-\tfrac32g(a)-\tfrac32g(b).
 \tag{1}
\]
Here \(s_*\) is the original zero-lift type-four conditional root.
The [full right-square source theorem](research_mixed_unselected_right_taper_products.md),
Theorem 1, proves its nonzero original finite-sum packet on the product
of two copies of \([.22,.50]+i[-.057,.0141]\). The original logarithmic
branches, not just their exponentiated polynomial equations, are used below.

The actual homogeneous-four point is
\[
 z_*=r+ih_*=\frac{i}{2\pi}\Log\frac{-1-i\sqrt7}{4}.
 \tag{2}
\]
It is the homogeneous zero-lift solution of the
[cyclic localization theorem](research_mixed_cyclic_critical_localization.md).
In particular \(s_*(z_*,z_*)=z_*\) and the cyclic outer gradient is
zero. All rates below use the absolute normalization (1).

## 1. A positive raw-row defect inside the left taper

Let
\[
 x=\frac{219}{1000},\quad y=\frac{173}{500},\quad
 u=\frac{57}{200},\qquad
 a=x+ih_*(x/.22)^2,\quad b=y+ih_*.
 \tag{3}
\]
Both target legs are unselected. Define
\[
 \begin{split}
 I_h(u,x)&=\Re g(x+u-i|h|)-\Re g(x-i|h|)
                                      +2\pi h_+u,\\
 E(u;a,b)&=I_{\Im a}(u,\Re a)+I_{\Im b}(u,\Re b)-3J(u)
       -2\pi(\Im a)u-\tfrac12\Re g(a)-\tfrac12\Re g(b),\\
 \Gamma(a,b)&=\phi(z_*,z_*)+\phi_a(z_*,z_*)(a-z_*)
                                +\phi_b(z_*,z_*)(b-z_*).
 \end{split}
 \tag{4}
\]
Here \(J(u)=\Re g(u)\) for \(0<u<1\).

**Proposition 1.** The original raw-row envelope at (3) satisfies
\[
                 E(u;a,b)-\Re\Gamma(a,b)>\frac{9}{500}.
 \tag{5}
\]
Thus the geometric supporting-plane upper bound cannot be proved by
taking absolute values of the original inner rows throughout the left
taper.

The checker evaluates (4) directly with outward arithmetic. These
expressions also have their literal finite-source meaning. In the
canonical Laurent kernel
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
          \frac{X^{-j}(r_NX;r_N)_j(r_NY;r_N)_j}{(r_N;r_N)_j^3},
 \quad r_N=e^{-2\pi i/N},
 \tag{6}
\]
take \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\) and
\(j/N\to u\). The logarithmic modulus of this row, divided by \(N\),
tends to the first four terms of \(E\). The numerator factors stay
away from zero because both heights are negative; the denominator
uses the usual sine-factorial estimate, whose logarithmic error is
\(O(\log N)\). The half-weights in (4) are genuine as well:
the [Fourier-weight theorem](research_mixed_fourier_weight_continuation.md),
Theorem 1, gives the relative asymptotic of \(d_N\) at both target
points since their real parts lie in \((0,1/2)\) and their heights
are nonpositive. Hence the allocated positive raw sum itself exceeds
the tangent-plane rate, at both parities. This does not assert that
the coherent kernel exceeds that plane.

## 2. A full reset at .22 can raise the coherent cyclic rate

Consider the all-four cyclic word of length seven. Use target
coordinates
\[
 w_0=.22,\qquad w_1=w_6=r,\qquad
 w_2=w_3=w_4=w_5=z_*.
 \tag{7}
\]
These are the values of the proposed nearest-neighbor height graph
\[
 H_j=h_*\rho(x_{j-1})\rho(x_j)\rho(x_{j+1})
 \tag{8}
\]
at \(x_0=.22\), \(x_j=r\) otherwise, whenever
\(\rho(.22)=0\) and \(\rho(r)=1\).
The [exact coupled graph theorem](research_mixed_coupled_outer_graph.md)
permits this deformation, but does not supply a support bound on it.

**Proposition 2.** At (7),
\[
 \frac{93}{10000}<
 \Re\left\{\sum_{j=0}^6\phi(w_{j-1},w_j)-7\phi(z_*,z_*)\right\}
 <\frac{95}{10000}.
 \tag{9}
\]
Consequently an absolute pointwise domination by the original
geometric rate fails on this graph.

Only four block values differ from the homogeneous value:
\[
 (r,.22),\quad(.22,r),\quad(r,z_*),\quad(z_*,r).
 \tag{10}
\]
The checker encloses their original logarithmic roots by explicit
Newton self-maps, fixes the zero lift by the original residual, and
evaluates (9). All points and pairs are in the already proved source
domain of (1). Moreover every leg is in
\(0<\Re w<1/2,\Im w\le0\), so the actual Fourier weight is relatively
asymptotic to its factorial interpolant.

In detail, let the unaliased original cyclic density, with its
irrelevant overall carrier omitted, be
\[
 D_N(w)=\prod_{j=0}^6
 C_{1,N}(e^{-2\pi iw_{j-1}},e^{-2\pi iw_j})
 d_N(e^{-2\pi iw_j}).
 \tag{11}
\]
The nonzero packets and relative weight comparisons give
\[
 \lim_{N\to\infty}\frac1N\log|D_N(w)|
                  =\Re\sum_{j=0}^6\phi(w_{j-1},w_j).
 \tag{12}
\]
All half-weights have recombined into the literal integer powers
in (11). Thus (9) concerns the actual finite density, not an
unrepresented continuation of a saddle. Since every fixed source
packet is valid on a neighborhood, the strict excess also persists
near the specified target points. The cyclic integral can still
have cancellations; neither (9) nor (12) rules out a different
contour or a coherent treatment of its remaining variables.

## Reproduction

The focused checker validates the exact homogeneous algebra, all four
original logarithmic Newton maps, the raw-row inequality, the coherent
rate interval, and the source-record bindings. Its proposed decimal
root centers carry no acceptance authority.

    python3 experiments/check_mixed_left_support_obstructions.py --precision 256
