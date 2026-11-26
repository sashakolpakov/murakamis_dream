# Boundary multiplication preserves concentrated original sources

Multiplication by a fixed crossing power preserves a boundary asymptotic
when the original boundary polynomial has a strict angular decay bound.
The multiplication is performed in the full Hermite quotient. Its
canonical polynomial is exponentially close, on the real physical
period and on a smaller complex disk, to the product with the original
Gaussian representative of that crossing.

The angular decay assumption is essential. The crossing polynomial by
itself has exponentially large band-edge terms on a complex strip, as
shown in the [polynomial crossing calculation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_polynomial_crossing_fourier_trace.md).
The proof here suppresses those terms using the decay of the factor
being multiplied. An unrestricted analogous assertion for the
quarter-turn is false; Section 7 gives an original-source counterexample.

## 1. Statement for the original quotient

Let
\[
 D=N-1,\qquad \eta=(-1)^D,\qquad
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad z(t)=-2\cos t.
 \tag{1}
\]
The Chebyshev polynomial has its ordinary normalization. Every double
root retains its first derivative; at odd levels the root \(-2\) is
simple. Write \(\operatorname{can}\) for the representative of degree
less than \(N\), and let \(R\) be the original crossing.

Suppose \(F_N(t)=f_N(-2\cos t)\), where \(\deg f_N<N\), is an original
boundary source. Assume that there are constants \(c,b>0\), \(B\ge0\),
\(C>0\), \(d\ge0\), and \(M\in\mathbb R\), independent of \(N\), such
that
\[
 |F_N(x+iy)|\le C N^d
   \exp N\{M-c(1-\cos x)+B y^2\},
 \qquad |x|\le\pi,\quad |y|\le b.                    \tag{2}
\]
Polynomial prefactors and the starting level may depend on the fixed
source. For a fixed signed integer \(n\), define
\[
 \begin{split}
 P_{n,N}(t)&=\operatorname{can}(R^n f_N)(-2\cos t),\\
 C_{N,n}&=\exp\left(\frac{\pi i nD^2}{4N}\right),\\
 g_{n,N}(t)&=C_{N,n}\exp\left(\frac{inNt^2}{4\pi}\right)F_N(t).
 \end{split}                                                   \tag{3}
\]
Negative powers in the first line are taken in \(\mathcal A_N\), before
choosing the representative. The scalar in the second line has the
displayed logarithm convention, not a principal fractional power of
another numerical scalar.

**Theorem 1.** Under (2), there are \(\delta>0\), \(r>0\), and fixed
polynomial prefactors such that
\[
 \sup_{|t|\le\pi,\ t\in\mathbb R}
 |P_{n,N}(t)-g_{n,N}(t)|
       \le C_nN^{d_n}e^{N(M-\delta)},                    \tag{4}
\]
and
\[
 \sup_{|t|\le r}|P_{n,N}(t)-g_{n,N}(t)|
       \le C_n'N^{d_n'}e^{N(M-\delta/2)}.                \tag{5}
\]
The constants \(\delta,r\) can be chosen using only \(c,B,b,n\).
Both estimates preserve all physical first normals and hold at both
parities of \(N\).

Suppose in addition that on a fixed complex disk
\[
 F_N(u)=\epsilon_N N^\alpha A(u)e^{NW(u)}(1+O(N^{-1})),\qquad
 |\epsilon_N|=1,                                       \tag{6}
\]
uniformly, where \(W\) is even and holomorphic, \(A\) is holomorphic
and nonzero, \(\Re W(0)=M\), and \(-\Re W''(0)>0\). Then, on a possibly
smaller fixed disk,
\[
 \boxed{\displaystyle
 P_{n,N}(u)=\epsilon_N C_{N,n}N^\alpha A(u)
   \exp N\left\{W(u)+\frac{in u^2}{4\pi}\right\}
                         (1+O(N^{-1})).}               \tag{7}
\]
It also satisfies a bound of the form (2), with positive constants
\(c',b'\) and a finite \(B'\). Thus the class of these concentrated
original boundary sources is closed under every fixed signed boundary
crossing multiplication.

No uniformity as \(n\) grows with \(N\) is asserted. A family with
common constants in (2), a common disk for the full expansion (6) on
which every amplitude is nonzero, common bounds on the normalized
phases \(W-W(0)\), and a common positive curvature bound has common
output constants for each fixed finite set of powers \(n\). Amplitude
sizes, error constants and starting levels may still depend on the
individual source.

## 2. Exact Hermite folding of a smooth periodic function

The physical angles are
\[
                 \tau_j=\frac{\pi(D-2j)}N,
                    \qquad j=0,\ldots,D.               \tag{8}
\]
The original crossing has the value and angular derivative of
\(C_{N,n}e^{inNt^2/(4\pi)}\) at these angles. Therefore the canonical
product in (3) has exactly the values and angular derivatives of
\(g_{n,N}\) there. At the odd simple angle zero, the angular derivative
vanishes by evenness and adds no spurious condition.

Let \(f\) be an even smooth periodic function with Fourier coefficients
\(a_\ell\), with enough decay that its value and first derivative series
converge absolutely. Let \(p(t)=\sum_{|m|<N}b_me^{imt}\), \(b_{-m}=b_m\),
be its full physical Hermite interpolant. Sampling on (8) gives
\[
 V_m=\sum_{k\in\mathbb Z}\eta^k a_{m+kN},\qquad
 W_m=\sum_{k\in\mathbb Z}(m+kN)\eta^k a_{m+kN}.         \tag{9}
\]
For \(1\le m<N\), the two band coefficients in this residue class obey
\(V_m=b_m+\eta b_{m-N}\) and
\(W_m=mb_m+\eta(m-N)b_{m-N}\). Hence
\[
 b_m=\sum_{k\in\mathbb Z}(k+1)\eta^k a_{m+kN}.
                                                               \tag{10}
\]
At \(m=0\), the derivative sample mean is zero by evenness, and
\[
 b_0=\sum_k\eta^k a_{kN}
       =a_0+2\sum_{k\ge1}\eta^k a_{kN}.                \tag{11}
\]
The same expression (10) also gives (11), after pairing \(k\) and
\(-k\). This includes every alias and the repeated-root derivatives.

The term \(k=-1\) in (10) is zero. All other terms apart from
\(a_m\) have \(|m+kN|\ge N\). Summing their absolute values, and
including the discarded original Fourier coefficients, gives
\[
 \|p-f\|_{L^\infty(\mathbb R)}
 \le C_0\sum_{|\ell|\ge N}
             (1+|\ell|/N)|a_\ell|.                    \tag{12}
\]
Here \(C_0\) is absolute. This is the general version of the exact
two-mode calculation in the polynomial crossing note. In particular,
value interpolation alone would not prove (12).

## 3. The endpoint cutoff and the complete Fourier tail

We suppress the subscript \(n,N\) temporarily. Since
\(1-\cos x\ge2x^2/\pi^2\) on \([-\pi,\pi]\), completing a square gives
\[
 \frac{|nxy|}{2\pi}
 \le\frac c2(1-\cos x)+\frac{n^2y^2}{16c}.
\]
Thus the analytic function \(g\) satisfies
\[
 |g(x+iy)|\le C N^d
   \exp N\{M-(c/2)(1-\cos x)+B_*y^2\},\qquad
 B_*=B+\frac{n^2}{16c}.                                \tag{13}
\]

Choose an even smooth cutoff \(\chi_N\) which is one on
\(|t|\le a_N=\pi-3\pi/(4N)\), zero on
\(|t|\ge b_N=\pi-\pi/(4N)\), and whose fixed derivatives are bounded
by \(C_jN^j\). Such cutoffs are obtained by rescaling one fixed smooth
function. The last physical angle is \(\pi-\pi/N<a_N\), so
\[
                         f(t)=\chi_N(t)g(t)             \tag{14}
\]
has exactly the same values and first derivatives at every physical
angle. Extending it periodically gives an even smooth function. Its
Hermite interpolant is consequently exactly \(P_{n,N}\), not a new
model for that polynomial.

Choose a fixed height \(h>0\) so small that
\[
 h<b/4,\qquad B_*h\le1/4,\qquad B_*h^2\le c/8.         \tag{15}
\]
Conditions containing \(B_*\) are vacuous if it is zero. Cauchy's
estimate on disks of radius \(1/(10N)\), with a slightly larger
height bound if needed, shows that each fixed derivative of \(g\)
costs only a fixed power of \(N\) in (13). These disks stay inside the
original real window at every point used in the cutoff and central
contour. Errors of size \(O(1/N)\) in the exponent are absorbed in the
constant.

Integrate the Fourier coefficient of (14) by parts four times.
There are no endpoint terms because the cutoff is zero near the ends
of the period. Terms with a derivative of \(\chi_N\), and the part
of \(\chi_Ng^{(4)}\) outside \([-a_N,a_N]\), lie in the endpoint
layers. On those layers \(1-\cos x\ge1\), so their total contribution
before the factor \(|\ell|^{-4}\) is bounded by
\(C_nN^{d+4}e^{N(M-c/4)}\).

For the remaining integral of \(g^{(4)}e^{-i\ell t}\), move
\([-a_N,a_N]\) to height \(-\operatorname{sgn}(\ell)h\). This is an
ordinary holomorphic deformation on this central rectangle. Its
horizontal part is bounded by
\[
 C_nN^{d+4}e^{N(M+B_*h^2)-|\ell|h}.
\]
Both vertical sides have \(1-\cos a_N\ge1\). Equations (13),(15)
bound them by \(C_nN^{d+4}e^{N(M-c/4)}\); the Fourier factor decreases
along each vertical side. In particular those sides have been
estimated, not discarded. Altogether, for \(|\ell|\ge N\),
\[
 |a_\ell|\le
 \frac{C_nN^{d+4}}{|\ell|^4}
 \left[e^{N(M+B_*h^2)-|\ell|h}+e^{N(M-c/4)}\right].    \tag{16}
\]
Since \(B_*h^2\le h/4\), summation gives
\[
 \sum_{|\ell|\ge N}(1+|\ell|/N)|a_\ell|
       \le C_nN^{d+1}e^{N(M-\delta)},\qquad
          \delta=\min(h/2,c/8)>0.                       \tag{17}
\]
Increasing a polynomial prefactor does not affect the fixed gap.
Equations (12),(17), together with the exponentially small difference
between \(f\) and \(g\) in their endpoint layers, prove (4).

The cutoff is used solely to estimate Fourier coefficients. It is not
continued to a complex domain, and it does not replace the original
finite source in any subsequent trace.

## 4. Local complex comparison

Set \(E_N=P_{n,N}-g_{n,N}\). This is analytic near the whole real
window. The real bound (4) holds, whereas (2)--(4) also give the crude
bound \(\sup_{\mathbb R}|P_{n,N}|\le C_nN^{d_n}e^{NM}\).
Each of its Fourier coefficients is therefore bounded by the latter
quantity. Its band \(|m|<N\) implies
\[
 |P_{n,N}(x+iy)|\le C_nN^{d_n+1}e^{N(M+|y|)}.           \tag{18}
\]

Fix \(a<\min(b/2,\pi/2)\). On the semicircle \(|z|=a\), (13),(18)
give
\[
 |E_N(z)|\le C_nN^{d_n'}e^{N(M+C_a)},\qquad
                    C_a=\max(a,B_*a^2).               \tag{19}
\]
On its real diameter the exponent is \(M-\delta\). In the upper
half-disk, the harmonic measure of the curved boundary is explicitly
\[
 \omega(z)=\frac2\pi\arg\frac{a+z}{a-z}.
\]
For \(|z|\le a/2\), it is at most
\(16\Im z/(3\pi a)\). The two-constants inequality for the subharmonic
function \(\log|E_N|\) therefore gives exponent
\[
                  M-\delta+(\delta+C_a)\omega(z).
\]
The lower half-disk has the identical estimate with \(|\Im z|\).
Choose
\[
 r\le\min\left(a/2,\frac{3\pi a\delta}{32(\delta+C_a)}\right).
                                                               \tag{20}
\]
Then (5) follows. This argument uses the analytic function \(E_N\),
not the smooth Fourier periodization.

Under (6), shrink this disk once more so that
\(\Re(W(u)+inu^2/(4\pi))\ge M-\delta/4\) there. The amplitude is
bounded away from zero on a smaller closed disk. The error (5) is
then exponentially small relative to the main term, proving (7).
The same argument works uniformly for a family with the common phase
bounds stated after the theorem. No common positive lower bound on
the amplitudes is required: each fixed source has its own starting
level.

## 5. Recovering a whole-period Gaussian strip bound

On the real period, (4) and (2) immediately imply
\[
 |P_{n,N}(x)|\le C_nN^{d_n}
       e^{N\{M-c_1(1-\cos x)\}},\qquad
                    c_1=\min(c,\delta/2)>0.            \tag{21}
\]
Near zero the new phase in (7) has exactly the old real curvature:
\[
 -\Re\left(W''(0)+\frac{in}{2\pi}\right)=-\Re W''(0)>0.
\]
Its evenness and a fixed bound on its higher derivatives give, on a
small fixed complex disk,
\[
 \Re\left(W(x+iy)+\frac{in(x+iy)^2}{4\pi}\right)
                         \le M-a x^2+B_1y^2            \tag{22}
\]
for some \(a>0\), \(B_1<\infty\). For example, bound the mixed term
from the imaginary quadratic coefficient by completing a square, then
absorb higher terms by shrinking the disk. Formula (7) gives the same
bound for the source, with a polynomial prefactor.

For clarity, the far-angle strip can be obtained without continuing
the exponentially small interpolation error. Fix a small \(r_0>0\)
inside this local disk. The spectral interval
\(J=[-2\cos(r_0/2),2]\) corresponds to real angles
\(r_0/2\le|x|\le\pi\). On \(J\), (21) has a fixed gap
\(\Delta=c_1(1-\cos(r_0/2))\). Expanding the degree-\(D\) polynomial
in rescaled Chebyshev polynomials bounds its complex value by
\[
 2N\sup_J|P_{n,N}|\,e^{NG_J(z)},
\]
where
\(G_J(z)=\log|\zeta+\sqrt{\zeta^2-1}|\) is zero on \(J\),
\(\zeta\) being the affine coordinate taking \(J\) to \([-1,1]\),
and the exterior branch is used. This elementary Chebyshev estimate
is the interval Bernstein--Walsh bound used in the earlier source
proofs. Continuity of \(G_J\) makes it at most \(\Delta/4\) on
\(z=-2\cos(x+iy)\), \(r_0\le|x|\le\pi\), for a fixed sufficiently
small \(|y|\le b'\). This remains true at the endpoint \(z=2\).

Thus the far-angle strip retains a fixed gap. Combine it with (22),
choosing \(c'>0\) smaller than both the local quadratic constant and
\(\Delta/8\), and taking \(B'\ge B_1\). This proves the asserted
bound (2) for the canonical product on one fixed whole-period strip.
All choices are uniform under common input constants and local phase
bounds; there is no iteration over the level.

The same proof also handles a fixed finite product of concentrated
boundary sources. More precisely, if \(F_{j,N}\), \(1\le j\le s\),
satisfy (2),(6), then
\[
 \operatorname{can}\left(R^n\prod_{j=1}^s f_{j,N}\right)(-2\cos u)
 =C_{N,n}\left(\prod_j\epsilon_{j,N}\right)
 N^{\sum_j\alpha_j}\left(\prod_j A_j(u)\right)
 \exp N\left\{\sum_jW_j(u)+\frac{inu^2}{4\pi}\right\}
 (1+O(N^{-1})).                                        \tag{22a}
\]
This canonical product also has a whole-period Gaussian bound. To
verify the claim directly, use the analytic function
\(C_{N,n}e^{inNt^2/(4\pi)}\prod_jF_{j,N}(t)\) in Sections 2--4.
Its input constants are \(M=\sum M_j\), \(c=\sum c_j\), and
\(B=\sum B_j\). The input product need not have degree less than
\(N\): only the output Hermite interpolant needs that band, and its
physical jets are exactly those of the original quotient product.
The local real curvatures add, so Section 5 applies as well. The
number of factors and their powers are fixed before \(N\) tends to
infinity. This proves closure under multiplication and fixed crossings;
it still makes no assertion about the turn.

## 6. Actual families to which the theorem applies

The hypotheses are already proved for every terminal source
\(H_{p,N}\), \(|p|\ge2\), with common phase, angular and strip constants
in the [uniform terminal-family theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_uniform_terminal_family_and_star_fillings.md).
They are also proved for the one-boundary pieces in the
[recursive high-valence theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_recursive_high_valence_source.md).
Consequently arbitrary fixed boundary crossing powers can be attached
to any of those actual pieces without losing its full boundary
asymptotic or its strict angular bound.

A useful application concerns a pendant chain of \(k\ge1\) vertices,
all of power \(2\sigma\), \(\sigma=\pm1\). Its exact quotient identity
is proved in the [marked chain reduction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_repeated_two_crossing_chain_reduction.md):
\[
 F_{k,\sigma,N}=\kappa_N^{\sigma k}
           R^{-\sigma}H_{-\sigma(k+1),N},\qquad
 \kappa_N=\exp\frac{\pi iD^2}{2N}.                     \tag{23}
\]
Apply Theorem 1 to its canonical representative. On a common fixed
disk, for each fixed \(k\),
\[
 \boxed{\displaystyle
 F_{k,\sigma,N}(u)=
 \kappa_N^{\sigma k}C_{N,-\sigma}\epsilon_{-\sigma(k+1),N}
 A_{-\sigma(k+1)}(u)
 \exp N\left\{W_{-\sigma(k+1)}(u)
                         -\frac{\sigma i u^2}{4\pi}\right\}
 (1+O_k(N^{-1})).}                                     \tag{24}
\]
The common real angular gap, complex strip and normalized phase
bounds can be chosen independently of \(k\): the terminal family is
uniform and the new boundary multiplier is only \(R\) or \(R^{-1}\).
The amplitude and its error constant may depend on \(k\).

This strengthens the earlier quotient reduction to an asymptotic of
the actual canonical free-boundary polynomial. The existing marked
tangle identity still supplies the geometric interpretation after
attachment. Formula (24) does not identify the turn of an arbitrary
packet, solve a general low-valence connected region, or justify
discarding any current in a subsequent trace. Those operations still
need their own estimates.

## 7. Why unrestricted closure under turns is false

The turn problem cannot be solved by proving that every concentrated
source stays concentrated. For any fixed \(|p|\ge2\), the actual
terminal source is
\[
                         H_{p,N}=T(R^p).
\]
It satisfies the hypotheses of Theorem 1. But the original turn is
the Newton reversal, so \(T^2=I\) in the full algebra and
\[
                         T(H_{p,N})=R^p.                \tag{25}
\]
Let \(r_{p,N}(t)=\operatorname{can}(R^p)(-2\cos t)\). Its exact
physical values are
\[
 r_{p,N}(\tau_j)=C_{N,p}e^{ipN\tau_j^2/(4\pi)},
              \qquad |r_{p,N}(\tau_j)|=1.              \tag{26}
\]
This excludes concentration of the kind used here, regardless of the
rate one attempts to assign to it.

Indeed choose a physical angle \(t_N\) nearest zero: it is zero at
odd levels and has magnitude \(\pi/N\) at even levels. If a nonzero
local asymptotic (6) existed for this polynomial, its even phase and
nonzero amplitude would give
\[
 0=\log|r_{p,N}(t_N)|
   =N\Re W(0)+\alpha\log N+\log|A(0)|+O(N^{-1}).       \tag{27}
\]
Dividing by \(N\) forces \(M=\Re W(0)=0\). In particular a positive
rate is incompatible with the nonzero local expansion. A negative
rate is already incompatible with (2) at these same near-zero nodes.

Now fix any \(t_0\in(0,\pi)\), and choose physical nodes
\(s_N\to t_0\). At rate zero, a real angular bound (2) with \(c>0\)
would require
\[
 1=|r_{p,N}(s_N)|\le C N^d e^{-Nc(1-\cos s_N)},         \tag{28}
\]
whose right side tends to zero. This is a contradiction at both
parities. Thus a source in the proved class can leave that class
after a single turn.

A useful next theorem must therefore control the actual composed
source and its relevant hyperbolic, nondegenerate geometry, with
hypotheses that exclude this example. It cannot assert closure under
all turns. This counterexample does not disprove a volume identity
for a hyperbolic closure; it identifies a false unrestricted
intermediate claim. Neither hyperbolicity alone nor a local geometric
critical point has been shown here to supply the missing global
source estimate.

## 8. Reproducing the finite normalization checks

Run

```sh
python3 experiments/check_boundary_crossing_packet_preservation.py \
  --precision 120 \
  --output repro/results/research-boundary-crossing-packet-preservation.json
```

The [script](../experiments/check_boundary_crossing_packet_preservation.py)
compares multiplication by the original triangular Newton crossing
matrices with the Hermite Fourier reconstruction from the Gaussian
values and all angular derivatives. It uses the full bare-edge source
and the two actual terminal sources of powers \(2,-3\), at every
level \(2\le N\le12\), for multiplying powers \(-3,-1,1,2\).
The 132 level/source/power cases agree at 120-digit precision; the
largest relative physical-jet discrepancy is below \(3.0\cdot10^{-117}\),
and the largest off-grid reconstruction discrepancy is below
\(2.4\cdot10^{-119}\).

The [saved output](../repro/results/research-boundary-crossing-packet-preservation.json)
also records 24 comparisons of the actual canonical product with the
chirped source at levels \(16,17,32,33,64,65\), on sampled real angles
and two complex angles. These include the two signs of the pendant
chain with two power-two vertices. Those finite comparisons check the
normalization and illustrate the off-grid error. The exponential
estimate, its uniformity, and the whole-source conclusions follow
from the proof above, not from these samples.
