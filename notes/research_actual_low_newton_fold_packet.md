# The actual low-Newton kernel at its cubic wire fold

Private written proof, 17 November 2026.

The endpoint geometric series for the low-Newton kernel becomes
singular at the stationary wire fold. The original finite sum has
a uniform replacement there: an oriented half-line cubic integral,
with its finite normalization, both level parities and its endpoint
term retained. This supplies a local transition beyond the
middle-index dominance estimate. It does not estimate the rest of
an original network contour.

## 1. The original finite kernel and the fold

Use the complete direct sources [L] and [U] listed below. Write
\[
 N\ge2,\quad d=N-1,\quad L=d-\lfloor N/2\rfloor,\quad
 \nu_N=N/2-L=
 \begin{cases}1&N\ \mathrm{even},\\1/2&N\ \mathrm{odd},\end{cases}
\]
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 S_k=\prod_{j=1}^k2\sin(j\pi/N),\qquad
 e_k(w)=S_k^{-2}\prod_{j<k}(c_j-w).
 \tag{1}
\]
The actual low kernel is
\[
 K_N^{\mathrm{low}}(w,w')=\sum_{k=0}^{L}e_k(w)e_k(w').
 \tag{2}
\]
Thus the odd middle polynomial stays in (2), whereas the even
middle polynomial belongs to the high radical. No trace or
co-source has been changed.

The endpoint expression [L](4),(5) has denominator
\[
 1-r(h)r(h'),\qquad
 r(h)=\operatorname{sech}^2(h/2)=\frac4{w+2},
 \qquad w=2\cosh h.
 \tag{3}
\]
This denominator identifies a genuine stationary-wire fold.
Indeed, with \(w=-2\cos t,\ w'=-2\cos u\), the original
stationary relation [U](25)--(28) gives
\[
 q_e^2=1+\tan^2(t/2)+\tan^2(u/2)
   =\frac{16-(w+2)(w'+2)}{(2-w)(2-w')}.
 \tag{4}
\]
Consequently the zero in (3) is precisely \(q_e^2=0\), provided
the displayed denominators are nonzero. Its stationary wire is
\(x=1/2\). This is a fold of the wire stationary projection,
not a full angular/filling stationary equation.

We treat the whole real fold family
\[
            w_0=-2-4p,\qquad w'_0=-2-4p^{-1},
                         \qquad p>0,
 \tag{5}
\]
and a complex normal neighborhood on its natural finite-level
scale. Neither (5) nor the theorem below selects a knot diagram.

## 2. Uniform finite-source statement

Fix a compact interval \(P=[p_-,p_+]\subset(0,\infty)\).
There is a complex neighborhood \(U\) of \(P\) such that the
following assertions hold uniformly for \(p\) in compact subsets
of \(U\) and \(\zeta\) in arbitrary fixed complex compact sets.
Put
\[
 \epsilon_N=N^{-2/3},\qquad
 p'_N=p^{-1}e^{-\zeta\epsilon_N},\qquad
 w=-2-4p,\quad w'_N=-2-4p'_N,
 \tag{6}
\]
\[
 \kappa(p)=\frac{\pi^2}{3}(2+p+p^{-1}),\qquad
 I_p(\zeta)=\int_0^\infty
                   \exp\{\zeta s-\kappa(p)s^3\}\,ds .
 \tag{7}
\]
Choose \(U\) small enough that \(\Re p,\Re p^{-1}\) and
\(\Re\kappa(p)\) are positive. The integral is then holomorphic
in \(p,\zeta\), and entire in \(\zeta\).

**Theorem.** At both level parities,
\[
 \boxed{\quad
 \frac{K_N^{\mathrm{low}}(w,w'_N)}
      {N^{2/3}e_L(w)e_L(w'_N)}
       = I_p(\zeta)+O(N^{-2/3}).
 \quad}
 \tag{8}
\]
The error is holomorphic and has the same bound after every fixed
number of \(p,\zeta\) derivatives on smaller buffered compact
sets. The two finite polynomials in the denominator are the
original ones in (1); they are not normalized away from the
physical kernel.

For a fully displayed exponential normalization, define
\[
 H(p)=\operatorname{arcosh}(1+2p)
 \tag{9}
\]
by the holomorphic branch on \(\Re p>0\) which is positive
on the positive real axis. Both \(p\) and \(p'_N\) lie in
this half-plane for large \(N\), so both occurrences below
use that same specified branch. Then
\[
 \boxed{\quad
 N^{4/3}e^{-N\{H(p)+H(p'_N)\}/2}
       K_N^{\mathrm{low}}(w,w'_N)
       =\frac14 I_p(\zeta)+O(N^{-2/3}).
 \quad}
 \tag{10}
\]
The holomorphic error and derivative assertion also applies to
this normalized expression. At the fold,
\[
 I_p(0)=\frac{\Gamma(1/3)}{3\kappa(p)^{1/3}},
 \qquad
 K_N^{\mathrm{low}}(w_0,w'_0)
 =\frac{\Gamma(1/3)}
        {12\kappa(p)^{1/3}}\,
   N^{-4/3}e^{N\{H(p)+H(p^{-1})\}/2}
        (1+O(N^{-2/3})).
 \tag{11}
\]
The cube root in (11) is positive for real \(p>0\). In
particular the coefficient there is positive and nonzero.

## 3. Exact backward ratios and a global summable bound

For \(0\le j<L\) let
\[
 a_{N,j}=\cos^2((j+\nu_N)\pi/N),\qquad
 b_{N,j}=\sin^2((j+\nu_N+1/2)\pi/N).
 \tag{12}
\]
Directly from (1), for \(k=L-j\),
\[
 \frac{e_{k-1}(w)}{e_k(w)}
       =\frac{a_{N,j}}{p+b_{N,j}}.
 \tag{13}
\]
For example
\(c_{k-1}=-2+4b_{N,j}\) and
\(4\sin^2(k\pi/N)=4a_{N,j}\).
The ratio for \(w'_N\) uses \(p'_N\) instead of \(p\).
Thus the exact paired ratio and the entire normalized finite sum
are
\[
 R_{N,j}
 =\frac{e^{\zeta\epsilon_N}a_{N,j}^{\,2}}
        {(1+b_{N,j}/p)
         (1+p e^{\zeta\epsilon_N}b_{N,j})},
 \qquad
 \frac{K_N^{\mathrm{low}}(w,w'_N)}
      {e_L(w)e_L(w'_N)}
   =\sum_{\ell=0}^{L}\prod_{j=0}^{\ell-1}R_{N,j}.
 \tag{14}
\]
The empty product is one. These formulas retain the last
summand, the index zero, and the actual half-index displacement
at both parities.

On the parameter compacts in the theorem, all denominators in
(14) are units for large \(N\). More quantitatively, after
shrinking \(U\),
\(\Re(1/p)\ge c_0\) and
\(\Re(p e^{\zeta\epsilon_N})\ge c_0\).
For real \(b\ge0\), both associated factors \(1+zb\) have
modulus at least \(1+c_0b\).
Also, for \(0\le y<\pi/2\),
\(\log\cos y\le-y^2/2\).
It follows for every \(0\le\ell\le L\), with constants
independent of \(\ell,N\), that
\[
 \left|\prod_{j<\ell}R_{N,j}\right|
 \le \exp\{C\ell\epsilon_N-c\ell^3/N^2\}
 =\exp\{Cs-cs^3\},\qquad s=\ell\epsilon_N.
 \tag{15}
\]
Here \(\sum_{j<\ell}(j+\nu_N)^2\ge c'\ell^3\), including
\(\ell=1\). No intermediate summands have been discarded to
obtain this global bound.

## 4. Cubic expansion and the error in the finite sum

For \(j=o(N)\), use the logarithms continued from (14) at
positive \(p\) and \(\zeta=0\). Taylor expansion with uniform
remainders gives
\[
 \begin{split}
 \log R_{N,j}
 ={}&\zeta\epsilon_N
 -\frac{\pi^2}{N^2}
   \left[2(j+\nu_N)^2
       +(p+p^{-1})(j+\nu_N+1/2)^2\right]\\
 &+O\left(\frac{(j+1)^4}{N^4}
              +\epsilon_N\frac{(j+1)^2}{N^2}\right).
 \end{split}
 \tag{16}
\]
The second error includes the change from \(p\) to
\(p e^{\zeta\epsilon_N}\) in the denominator. Sum (16), put
\(s=\ell\epsilon_N\), and use
\(\sum_{j<\ell}j^2=\ell^3/3+O(\ell^2)\). Uniformly when
\(s\le N^{1/12}\),
\[
 \log\prod_{j<\ell}R_{N,j}
   =\zeta s-\kappa(p)s^3+E_{N,\ell},\qquad
 |E_{N,\ell}|
       \le C\epsilon_N(s+s^2+s^3+s^5).
 \tag{17}
\]
In this range the error is uniformly small; the extra \(s\)
term also covers the bounded smallest indices. The exact bound
(15), and the analogous bound for
\(\exp(\zeta s-\kappa s^3)\), show that replacing the products
by these exponentials in the scaled sum costs \(O(\epsilon_N)\).
For detail, on the range in (17) use
\(|e^E-1|\le |E|e^{|E|}\) and sum the resulting fixed
polynomial times \(e^{Cs-cs^3}\), with mesh \(\epsilon_N\).
Outside it, both tails are bounded by
\(C e^{-cN^{1/4}}\), after increasing \(N\).

Finally \(f(s)=e^{\zeta s-\kappa(p)s^3}\) obeys
\(\int_0^\infty|f'(s)|ds\le C\) on the parameter compacts.
The elementary left Riemann-sum estimate therefore gives
\[
 \left|\epsilon_N\sum_{\ell=0}^\infty
                 f(\ell\epsilon_N)-\int_0^\infty f(s)\,ds\right|
       \le C\epsilon_N.
 \tag{18}
\]
The tail beyond \(L\epsilon_N\) is exponentially small.
Equations (14)--(18) prove (8). All finite expressions are
holomorphic in the stated parameters, with no denominator zero;
the same argument on buffered compacts and Cauchy's formula
prove every fixed derivative assertion.

To obtain (10), the exact middle polynomials from [L](7), or
the same Chebyshev product calculation at negative colors, give
\[
 e_L(-2\cosh H)=
 \begin{cases}
 \displaystyle\frac{2\cosh(NH/2)}
          {N(\cosh H-\cos(\pi/N))},&N\ \mathrm{even},\\[2mm]
 \displaystyle\frac{\sinh(NH/2)}{N\sinh(H/2)},&N\ \mathrm{odd}.
 \end{cases}
 \tag{19}
\]
These are exact, including their signs. On the chosen complex
compacts \(\Re H\) is bounded below by a positive number.
Consequently, with \(p'_N\) as in (6),
\[
 N^2 e^{-N\{H(p)+H(p'_N)\}/2}e_L(w)e_L(w'_N)
 =
 \begin{cases}
 \displaystyle\frac1{4pp'_N}+O(N^{-2}),&N\ \mathrm{even},\\
 \displaystyle\frac1{4\sqrt{pp'_N}}+O(e^{-cN}),&N\ \mathrm{odd}.
 \end{cases}
 \tag{20}
\]
The square roots are continued from positive \(p,p'_N\).
Since \(pp'_N=e^{-\zeta\epsilon_N}\), each expression is
\(1/4+O(\epsilon_N)\). This proves (10), including all
holomorphic derivatives. Evaluating the integral at zero by
\(u=\kappa s^3\) proves (11).

## 5. The actual half-cycle, normal scale and geometric saddle

The integration direction in (7) is fixed by the original sum,
not selected by a saddle convention. Its variable is
\[
 s=N^{-2/3}(L-k)\ge0.
 \tag{21}
\]
Thus the low wire approaches \(x=k/N=1/2\) from below, with
\(x=1/2-N^{-1/3}s-\nu_N/N\).
Writing the original increasing-\(x\) sum as a Riemann integral
reverses both the limits and the sign of \(dx\). The coefficient
of the increasing \(s\) half-line is therefore \(+1\).

This is a relative half-cycle with its endpoint at \(s=0\).
Differentiation of (7) and integration by parts, justified by
its cubic decay, yield the exact equation
\[
                    3\kappa(p)I_p''(\zeta)-\zeta I_p(\zeta)=1.
 \tag{22}
\]
The right side is the retained endpoint contribution. Replacing
(22) by the homogeneous Airy equation would change this source.
For real \(p>0,\zeta\in\mathbb R\), the integrand in (7) is
positive; hence \(I_p(\zeta)>0\). On each compact such real
set it has a positive lower bound, which persists on a
sufficiently small complex neighborhood. No zero-free claim
on the whole complex \(\zeta\)-plane is made.

The relation to the original stationary wire is exact:
\[
 q_e^2=\frac{1-e^{-\zeta\epsilon_N}}
                  {(1+p)(1+p'_N)}.
 \tag{23}
\]
For real \(\zeta>0\), take
\(t=-iH(p),u=-iH(p'_N)\). The positive root of (23)
satisfies the original positive-edge criterion in [U].
The actual stationary wire
\(x_e^*=\pi^{-1}\arctan(1/q_e)\) therefore obeys
\[
 N^{1/3}(1/2-x_e^*)\longrightarrow
       \sqrt{\frac{\zeta}{3\kappa(p)}}.
 \tag{24}
\]
This is precisely the positive real stationary point of
\(\zeta s-\kappa(p)s^3\). Its real Laplace orientation is
positive. The real parameter ray is also a Stokes ray for
the full homogeneous cubic problem; (21),(22) do not assign
an ordinary complete-thimble intersection without the
relative endpoint.

The cubic coefficient can also be checked directly in the
original unsummed phase. Put
\(A=\cos^2(t/2), B=\cos^2(u/2)\) and
\(\delta=x-1/2\). Its continued derivative is
\[
 F_x=\Log\frac{(A-\sin^2\pi x)(B-\sin^2\pi x)}
                         {\sin^4\pi x}.
 \tag{25}
\]
Since \(A+B-AB=ABq_e^2\), near the fold it is
\[
 F_x=AB(\pi^2\delta^2-q_e^2)
       +O(\delta^4+|q_e^2|\,|\delta|^2+|q_e^2|^2).
 \tag{26}
\]
At \(q_e^2=0\) the cubic term of \(F-F(1/2)\) is
\(AB\pi^2\delta^3/3\). On (5),
\(AB=(1+p)(1+p^{-1})\), so (21),(23) turn this
primitive into exactly the exponent in (7). The proof of
(8), however, was the finite-product proof, not an inference
from this formal cubic.

For clarity, the derivative assertion in the theorem concerns
the scaled normal coordinate. At fixed \(N\),
\[
 \partial_\zeta=-N^{-2/3}(w'_N+2)\partial_{w'},\qquad
 p\partial_p=(w+2)\partial_w-(w'_N+2)\partial_{w'}
 \tag{27}
\]
on this two-parameter chart. Thus ordinary unscaled normal
derivatives have their actual \(N^{2/3}\) factors. Derivatives
of the full kernel additionally differentiate the exact
factors \(e_L(w)e_L(w'_N)\) in (8), or the exponential in
(10). Those terms are not discarded. Bounded holomorphic
outside parameter substitutions are covered by the buffered
derivative estimates. An arbitrary growing exterior attachment
still requires its own actual norm.

## 6. An actual overlap with the positive stationary wire

The compact-\(\zeta\) limit alone is not an overlap theorem at
fixed nonzero detuning. There is, however, a growing real
parameter range on which the actual finite sum connects to
the original positive Gaussian wire.

Let \(p\in P\) be real and suppose
\[
 \zeta=\zeta_N\longrightarrow+\infty,\qquad
       \epsilon_N\zeta_N^{5/2}\longrightarrow0.
 \tag{28}
\]
In particular \(\zeta_N=o(N^{4/15})\) suffices.
The definitions (6) are unchanged. All summands in (14)
are now positive. Uniformly in this regime,
\[
 \begin{split}
 \epsilon_N
 \frac{K_N^{\mathrm{low}}(w,w'_N)}{e_L(w)e_L(w'_N)}
 &= I_p(\zeta)
       \left\{1+O(\epsilon_N\zeta^{5/2})
                    +O(e^{-c\zeta^{3/2}})\right\},\\
 I_p(\zeta)
 &=\frac{\sqrt{\pi}}{(3\kappa(p)\zeta)^{1/4}}\,
   \exp\left\{\frac{2\zeta^{3/2}}{3\sqrt{3\kappa(p)}}\right\}
                  (1+O(\zeta^{-3/2})).
 \end{split}
 \tag{29}
\]
The first error includes the smaller Riemann-sum error.

Here is the relative estimate, including its tails. For
\(s=\ell\epsilon_N\le C_1\sqrt{\zeta}\), the same Taylor
calculation as (16), now retaining the size of \(\zeta\),
gives
\[
 \log\prod_{j<\ell}R_{N,j}
   =\zeta s-\kappa(p)s^3
      +O\{\epsilon_N(s+s^2+s^5+\zeta s^3)\}.
 \tag{30}
\]
The error is \(O(\epsilon_N\zeta^{5/2})=o(1)\)
on this whole interval. The bound (15) is now
\(\exp(\zeta s-cs^3)\), with \(c>0\) uniform in (28):
the denominator factors are positive and the cosine bound
is unchanged. Taking \(C_1\) sufficiently large makes its
tail beyond \(C_1\sqrt{\zeta}\) bounded by
\(C e^{-c'\zeta^{3/2}}\). The model integral has the same
tail property. The positive function
\(e^{\zeta s-\kappa s^3}\) is unimodal. Its scaled
Riemann sum differs from its integral by at most
\(2\epsilon_N\max_s e^{\zeta s-\kappa s^3}\).
Its integral is at least a fixed constant times
\(\zeta^{-1/4}\) times that maximum, by integrating on a
fixed multiple of its Gaussian width. Thus the relative
Riemann error is \(O(\epsilon_N\zeta^{1/4})\), absorbed
in (29). These estimates prove the first line there
without taking an absolute bound for an oscillatory sum.

For the second line set
\(s=\sqrt{\zeta/(3\kappa)}\,y\). The phase becomes
\[
 \frac{\zeta^{3/2}}{\sqrt{3\kappa}}
                     (y-y^3/3),\qquad y\ge0.
 \tag{31}
\]
It has a unique maximum at \(y=1\), negative second
derivative there, and a strict relative gap outside any
fixed neighborhood of that point. Taylor expansion and
Gaussian integration on that neighborhood give the
displayed prefactor and \(O(\zeta^{-3/2})\) relative
error; the cubic tails are integrable. All coefficients
are positive and the original real orientation is \(+1\).

The connection can be expressed using the actual wire
phase and its Hessian, without replacing them by their
cubic approximations. Set
\[
 A=1+p,\quad B=1+p'_N,\quad
 q=\sqrt{\frac{1-pp'_N}{AB}}>0,\qquad
 x_*=\pi^{-1}\arctan(1/q),
 \tag{32}
\]
and let \(\Delta F=F(x_*)-F(1/2)\) be the definite
integral from \(1/2\) to \(x_*\) of the literal derivative
\[
 F'(x)=\log
 \frac{(p+\cos^2\pi x)(p'_N+\cos^2\pi x)}
                         {\sin^4\pi x}.
 \tag{33}
\]
This is the real branch of (25), hence of the original
unsummed source. Its constant is not reset: the reference
normalization remains \(e_L(w)e_L(w'_N)\).
The exact Hessian from [U](28) is
\[
 H_e=-F''(x_*)=2\pi ABq(1+q^2)^2>0.
 \tag{34}
\]
Equations (26),(32), with \(C_0=2+p+p^{-1}\), give
\[
 \begin{split}
 q&=N^{-1/3}\sqrt{\zeta/C_0}
                           (1+O(\epsilon_N\zeta)),\\
 H_e&=2\pi N^{-1/3}\sqrt{C_0\zeta}
                           (1+O(\epsilon_N\zeta)),\\
 N\Delta F&=\frac{2\zeta^{3/2}}{3\pi\sqrt{C_0}}
                           +O(\epsilon_N\zeta^{5/2}).
 \end{split}
 \tag{35}
\]
For the last identity, integration of (26) up to
\(\delta_*=-q/\pi+O(q^3)\) gives
\(\Delta F=2ABq^3/(3\pi)+O(q^5)\).
All constants are uniform for \(p\in P\).
Substitution in (29) proves the actual overlap formula
\[
 \boxed{\quad
 K_N^{\mathrm{low}}(w,w'_N)
  =e_L(w)e_L(w'_N)\,
       e^{N\Delta F}\sqrt{\frac{2\pi N}{H_e}}\,
       \left\{1+O(\epsilon_N\zeta^{5/2})
                    +O(\zeta^{-3/2})\right\}.
 \quad}
 \tag{36}
\]
This is the original positive-wire Gaussian normalization
with coefficient \(+1\) in a proved overlap, rather than
only a formal identification of its stationary point.
The difference between \(L/N\) and \(1/2\) changes the
classical reference exponent by \(O(\epsilon_N\zeta)\);
the finite reference in (36) remains exact throughout.
Nothing here asserts an overlap at fixed macroscopic
detuning, or a globally preserved thimble coefficient
after other source variables and currents are integrated.

## 7. Source scope and coverage

The archived product-contour construction already identifies
the algebraic stationary fold and gives a pole-free finite
factorial contour through regular positive wire graphs. The
low-kernel source already proves geometric-series dominance
away from this fold. Neither statement supplies (8), its
half-line coefficient, the scale \(N^{-2/3}\), the
inhomogeneous endpoint term (22), or the relative overlap
with the original Gaussian normalization in (36).

The new result is a uniform asymptotic of the actual finite
low kernel on the entire family (5) and its bounded complex
normal scaling. The high radical in [L](2), its physical
value/normal matching contractions, original crossing
phases, angular trace kernels, aliases and final covector
remain exactly where the source puts them. No estimate for
their coherent sum follows from (8). In particular the
positive coefficient in (11) is a local kernel coefficient,
not the coefficient of a geometric period after closing.

The complete direct texts were read in full and their used
implications checked at the following pins:

* [L: The actual low kernel and its endpoint normalization](research_low_kernel_all_removed_current_asymptotic.md),
  SHA256 e9261e460fe52989ea298f423acc699a4e4b34c00805efbe52c5bee8eb2c1161.
* [U: The original unsummed phase and stationary wire](research_unsummed_network_phase_coercivity.md),
  SHA256 b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e.

The complete positive-wire product-contour proof and the
complete low complete-end and regular zero-subtree proofs
were also read for coverage; their different endpoint
estimates are not imported. This work used written
mathematics, source reads and metadata hashes only.
No mathematical program, numerical experiment, test or
build was run. Frozen notes and public papers are unchanged.
