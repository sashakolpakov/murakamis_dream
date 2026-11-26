# A fixed microscopic disk determines the joint growth rate

Research deduction, 6 November 2026.

A fixed-order meridian equation and a linear Laurent-degree bound
control joint complex growth from the function on one fixed
microscopic disk. The end coefficients may vanish at the complete
meridian, and their nearby roots may ramify or approach orbit points
arbitrarily closely. A common contour in the microscopic variable
avoids these roots before recurrence transfer. No vanishing factor
is deleted.

This strengthens the function-level conclusion of the
[singular orbit-jet theorem](research_regularized_singular_orbit_jet_growth.md).
The observation here is a whole disk norm, not a prescribed finite
jet block. It does not bound that norm by ordinary-color values.

## 1. Statement and actual-source scope

Put \(q_N=e^{\pi i/N}\), \(Q_N=q_N^2\) and
\(T_Nf(Y)=f(Q_NY)\). Suppose the Laurent polynomials \(R_N\)
satisfy, for a fixed integer \(A\ge1\) and \(G>0\),
\[
 \operatorname{supp}R_N\subset[-AN,AN],\qquad
                  \|R_N\|_{|Y|=1}\le e^{GN}
 \tag{1}
\]
eventually. Assume the exact fixed-order equation
\[
 \sum_{i=0}^d b_i(q_N,Y)R_N(Q_N^iY)=\beta_N(Y),
 \quad d\ge1,\quad
 b_i\in\mathbb C[q^{\pm1},Y^{\pm1}],
 \tag{2}
\]
where \(\beta_N\) has fixed Laurent support and polynomially
bounded coefficients. Require only the following classical end
condition:
\[
                 b_0(1,Y)\not\equiv0,\qquad
                 b_d(1,Y)\not\equiv0.
 \tag{3}
\]
There is no requirement that either value at \(Y=1\) be nonzero.
There is no analytic-branch hypothesis for the quantum zero divisors.
Condition (3) does retain the actual shift order; a classical loss
of an end coefficient is not covered.

Define
\[
 \begin{split}
 U_0&=\lim_{\delta\downarrow0}\limsup_{N\to\infty}
       \frac1N\log\sup_{|z|\le\delta}|R_N(e^z)|,\\
 R_*&=3+2\pi(d-1),\\
 \mathcal M_N&=1+\sup_{|\zeta|\le R_*}
                              |R_N(e^{\zeta/N})|,\qquad
 a_*=\limsup_{N\to\infty}N^{-1}\log\mathcal M_N .
 \end{split}
 \tag{4}
\]
The convention is \(\log0=-\infty\).

**Theorem 1.** Under (1)--(3),
\[
                            a_*=\max(0,U_0).
 \tag{5}
\]
Thus one fixed microscopic radius, determined by the recurrence
order, suffices. There is no supremum over growing radii or jet
orders in the observation (4).

The subsequent [radius-transfer lemma](research_subexponential_variation_meridian_observation.md),
Section 1, proves that any two fixed positive microscopic radii
have the same disk-norm exponential rate, using (1) alone.
Consequently \(R_*\) in the conclusion may be replaced by any
fixed positive radius. The classical end condition (3) and
the distinction from evaluation at the center remain unchanged.

The actual regularized knot period has (1)--(2), including its
polynomial affine source, by
[actual growth characteristics](research_regularized_period_growth_characteristics.md)
and the degree proof in
[orbit-jet growth](research_regularized_orbit_jet_growth.md), Section 5.
For a specified actual operator, (3) is still an operator condition
to check. The construction of the primitive normal operator only
proves that its entire classical symbol is nonzero; it does not
prove both conditions in (3). No statement about an unknown
geometric classical component is needed in this theorem.

## 2. A common microscopic circle avoids every nearby zero

Let \(p(q,Y)\) be either \(b_0(q,Y)\) or \(b_d(q,Y)\), and let
\(\mu\) be the order of its classical zero at \(Y=1\), with
\(\mu=0\) permitted. Choose a fixed small disk about \(Y=1\)
whose closure contains no other classical zero. On a smaller
fixed disk, for all sufficiently large \(N\),
\[
 p(q_N,Y)=u_N(Y)\prod_{r=1}^{\mu}(Y-\lambda_{N,r}),
 \qquad |u_N(Y)|\ge c>0,\qquad \lambda_{N,r}\longrightarrow1.
 \tag{6}
\]
The roots are counted with multiplicity and need not be labelled
analytically in \(q\).

Here is a direct justification of the uniform unit bound.
Uniform convergence to \(p(1,Y)\) on the larger disk boundary
fixes the number of roots inside it by the argument principle.
All these roots converge to \(1\); after dividing their monic
product, the remaining factor is holomorphic and zero-free.
On the fixed boundary, both the original function and the root
distances are uniformly bounded above and below. The maximum
principle applied to the reciprocal of the quotient supplies
the lower bound on a smaller disk. Laurent monomials are units
on these disks.

Use the logarithm near \(1\), and write
\[
                  w_{N,r}=\log\lambda_{N,r}.
 \tag{7}
\]
At orbit step \(j\), the microscopic variable is
\(Y=Q_N^j e^{s/N}\). The zeros supplied by this root are
\[
          s=Nw_{N,r}-2\pi i j+2\pi i N\ell,\qquad \ell\in\mathbb Z.
 \tag{8}
\]
As \(j\) ranges over the integers, these points lie on a vertical
lattice of spacing \(2\pi\). Each such lattice has at most three
points in \(|s|\le4\), because their imaginary parts lie in an
interval of length \(8<4\pi\).

Let \(D\) be the sum of the Laurent \(Y\)-spans of \(b_0\) and
\(b_d\). Both lists in (6) together have at most \(D\) roots.
There are therefore at most \(3D\) relevant zeros in
\(|s|\le4\), even if every transfer segment in the small parent
arc is considered at once. Put
\[
                   \varepsilon=\frac1{4(3D+1)}.
 \tag{9}
\]
Delete intervals of radius \(\varepsilon\) about the moduli of
these zeros from \([2,3]\). Their total length is less than
\(1/2\), so one can choose
\[
                         r_N\in[2,3]
 \tag{10}
\]
outside all the deleted intervals. On the whole circle
\(|s|=r_N\), the distance to every zero in (8) is at least
\(\varepsilon\). Zeros of modulus greater than \(4\) have
distance at least \(1\). The same radius works for both end
coefficients and for every consecutive transfer segment. It
depends on \(N\), but is used only for a maximum-modulus estimate.

Choose a fixed parent arc sufficiently small that all its
\(Q_N^j e^{s/N}\), for \(|s|\le3\), lie in the disk used in (6).
Other roots of \(p(q_N,Y)\) then play no role. This choice is
uniform in the smaller arc parameter introduced below.

## 3. A lattice product lower bound

For any \(a\in\mathbb C\) and \(n\) distinct consecutive integers
\(j\), suppose all \(|a+2\pi i j|\ge\varepsilon\).
Sort these distances as \(d_1\le\cdots\le d_n\).
Any \(k\) distinct points of the vertical lattice have vertical
span at least \(2\pi(k-1)\). If all lie in a disk of radius
\(d_k\) about zero, their vertical span is at most \(2d_k\).
Hence
\[
 d_1\ge\varepsilon,\qquad
 d_k\ge\pi(k-1)\ (k\ge2),\qquad
 \prod_j|a+2\pi i j|
       \ge\varepsilon\pi^{\,n-1}(n-1)! .
 \tag{11}
\]
The last inequality is valid for \(n=1\) as well.
It is uniform in the location of the lattice; no estimate on
the distance of an individual root from an orbit point is needed.

On the fixed parent disk, logarithmic and ordinary distances are
uniformly comparable. Thus, for \(|s|=r_N\) and steps in the
parent arc,
\[
 |Q_N^j e^{s/N}-\lambda_{N,r}|
      \ge \frac{c_1}{N}
                |s-Nw_{N,r}+2\pi i j|.
 \tag{12}
\]
For example, write the left side as
\(e^{w_{N,r}}|e^v-1|\), with
\(v=(s+2\pi i j)/N-w_{N,r}\).
The parent arc and disk can be chosen so that \(v\) lies in a
fixed disk on which \((e^v-1)/v\) is bounded away from zero.
This argument does not use the speed at which \(w_{N,r}\to0\).

Apply (11)--(12) to each root in (6), and retain the unit
factor. For every consecutive segment of \(n\ge1\) steps,
\[
 \prod_j |p(q_N,Q_N^j e^{s/N})|^{-1}
 \le c^{-n}
       \left[
          \frac{(N/c_1)^n}
               {\varepsilon\pi^{\,n-1}(n-1)!}
       \right]^\mu
                    \qquad(|s|=r_N).
 \tag{13}
\]
In particular, for \(n\le \alpha N/(2\pi)+O(1)\), with
\(0<\alpha<\alpha_*\) in a fixed sufficiently small parent arc,
\[
 \prod_j |p(q_N,Q_N^j e^{s/N})|^{-1}
 \le N^{C_0}\exp\!\left[
          C_1' N\alpha(1+|\log\alpha|)\right].
 \tag{14}
\]
This follows from
\(\log((n-1)!)\ge n\log n-n-O(\log(n+1))\).
The constants in (14) are independent of \(\alpha,N,s\).
They may be enlarged once for both end coefficients and the
bounded extra companion steps. An empty segment has product one.

Ramified roots with \(N|w_{N,r}|\to\infty\) are included:
their shifted lattice may meet the small \(s\)-disk at a distant
orbit step, but the common radius and product estimate already
include that step. Arbitrarily close nonzero lattice approaches
are handled by the same contour, rather than a Diophantine claim.

## 4. Whole-function transfer before taking jets

For fixed \(s\) collect the \(d\) consecutive values
\[
 V_j(s)=\bigl(
 R_N(Q_N^j e^{s/N}),\ldots,
 R_N(Q_N^{j+d-1}e^{s/N})\bigr)^t.
 \tag{15}
\]
Write (2) in companion form with \(b_d\) on the left for
forward propagation and \(b_0\) on the left for backward
propagation. On the circle (10) these divisions are legitimate,
by Section 2. Their complete numerator matrices are uniformly
bounded on the fixed parent disk.

For the affine source, choose a fixed power \(N^p\) bounding its
coefficients. Adjoin the constant coordinate \(N^p\), use
\(\beta_N/N^p\) in the source column, and put the leading
coefficient in the bottom-right numerator entry. The augmented
numerator matrices then have one fixed norm bound \(M\).
The initial augmented column on \(|s|=r_N\) has norm at most
a fixed polynomial in \(N\) times \(\mathcal M_N\), since
\[
 |s+2\pi i i|\le3+2\pi(d-1)=R_*\qquad(0\le i<d).
 \tag{16}
\]

Multiply these numerator matrices along each whole segment
and use (14) for its complete denominator product. It follows
that on the common circle
\[
 \max_{|\arg Q_N^j|\le\alpha}
 |R_N(Q_N^j e^{s/N})|
 \le C N^p e^{N\omega(\alpha)}\mathcal M_N,\qquad
 \omega(\alpha)=C'\alpha(1+|\log\alpha|).
 \tag{17}
\]
Forward and backward segments from \(0,\ldots,d-1\) cover this
arc; their bounded endpoint offsets are already included in (14).
The constants can be fixed on the parent arc, independently of
the smaller \(\alpha\).

The actual functions in (17) are entire in \(s\).
The maximum principle therefore gives the same bound on
\(|s|\le2\). Cauchy's estimate on \(|s|=1\) consequently gives,
for every fixed \(K\),
\[
 \max_{\substack{|\arg Q_N^j|\le\alpha\\0\le r<K}}
 |(N^{-1}Y\partial_Y)^rR_N(Q_N^j)|
       \le C_KN^p e^{N\omega(\alpha)}\mathcal M_N.
 \tag{18}
\]
Only \(C_K\), not the exponential rate cost, depends on \(K\).
No Taylor division at a zero has been used. The same fixed
microscopic observation controls all fixed derivative orders.

## 5. From the small arc to the joint complex envelope

Use the exact full-circle Hermite sampling inequality from
[orbit-jet growth](research_regularized_orbit_jet_growth.md),
Section 2. For Laurent support in \([-DN,DN]\), the first
\(2D+1\) scaled Euler jets at all orbit points bound the circle
norm and, at an unscaled logarithmic point \(z\), the function
by an additional factor \(C_DN e^{DN|\Re z|}\).
This finite Vandermonde statement retains the aliases \(Y^N-1\).

For fixed \(\alpha\), put
\[
 w(Y)=\frac{2+Y+Y^{-1}}4,\qquad \rho_\alpha=\cos^2(\alpha/2),
 \qquad G+L\log\rho_\alpha<-2
 \tag{19}
\]
with a fixed integer \(L>0\). Apply the Hermite inequality to
\(w^{LN}R_N\), of Laurent support
\([-(A+L)N,(A+L)N]\). The needed fixed number of jets is
\(2(A+L)+1\).
On the small arc, (18) and the finite product rule bound their
rate by \(a_*+\omega(\alpha)\).
Outside it, each fixed derivative of \(w^{LN}\) is bounded by
a fixed multiple of \(\rho_\alpha^{LN-r}\), while the jets of
\(R_N\) have rate at most \(G\), by (1) and its coefficient
Cauchy bound. Thus the outside rate is strictly negative.

Near \(z=0\), \(w(e^z)=\cosh^2(z/2)\), so division by
\(w(e^z)^{LN}\) costs at most \(CL|z|^2\) in normalized
logarithmic rate. The Laurent estimate costs at most
\((A+L)|\Re z|\). First let \(N\to\infty\), and then let the
unscaled \(z\)-disk shrink, keeping \(\alpha,L\) fixed. This proves
\[
                         U_0\le a_*+\omega(\alpha).
 \tag{20}
\]
For the converse, every fixed microscopic disk in (4) is
contained in any fixed unscaled \(z\)-disk for large \(N\).
Hence \(a_*\le\max(0,U_0)\). Since \(a_*\ge0\), (20) and
\(\omega(\alpha)\to0\) prove (5).
The observation radius \(R_*\) stays fixed as \(\alpha\downarrow0\);
only the auxiliary localization degree and the number of Cauchy
derivatives increase, each remaining fixed before the level limit.

## 6. What this supplies for the actual source

The actual canonical decomposition is
\[
 F_N=S_NR_N+P_N^{\rm col},\qquad
 N R_N(1)=K_N-P_N^{\rm col}(1),
 \qquad |P_N^{\rm col}(1)|\le\operatorname{poly}(N).
 \tag{21}
\]
Suppose (3) holds for a specified actual normal equation and
its independently controlled microscopic profile gives
\[
 \sup_{|\zeta|\le R_*}|R_N(e^{\zeta/N})|
                \le e^{o(N)}(1+|K_N|).
 \tag{22}
\]
Then (21), (22) and Theorem 1 imply the source-specific equality
\[
 \max(0,U_0)=
       \max\!\left(0,\limsup_N N^{-1}\log|K_N|\right).
 \tag{23}
\]
This criterion needs a function bound only on one fixed
microscopic disk. It needs neither analytic roots of the
end coefficients nor a comparison of meridian and quantum-normal jets.
Condition (22) remains a genuine source estimate; ordinary colors
and fixed quantum-normal initial jets do not imply it.

For the actual figure-eight, the specified calibrated order-three
normal operator has the end coefficients (20) of
[the singular orbit-jet note](research_regularized_singular_orbit_jet_growth.md).
They satisfy (3), although both vanish classically at \(Y=1\).
The already proved
[paired-factor microscopic profile](actual_paired_factor_meridian_profile.md),
Section 3, supplies
\[
 R_N(e^{\zeta/N})
   =\frac{K_N}{N}e^{-(N-1)\zeta/(2N)}
                         (1+O_{R_*}(N^{-1}))
 \tag{24}
\]
on the required disk. Thus this function-level theorem also yields
\[
                U_0=
             \frac{\operatorname{Vol}(S^3\setminus4_1)}{2\pi}.
 \tag{25}
\]
This is a second proof of the new joint-growth calibration using
the same known actual microscopic and complete-value asymptotics.
It does not reprove their volume theorem or assert a pointwise
asymptotic throughout a fixed unscaled neighborhood.

The unresolved operator issue for a general knot is now the
classical end condition (3), rather than analytic splitting of
its near-complete divisor. If that condition holds, the remaining
complete-value comparison is precisely a bound such as (22) on
the actual microscopic profile. The common meridian factors,
their nearby zeros, the affine source, and all central aliases
remain in the argument.
