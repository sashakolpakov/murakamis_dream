# A nonzero microscopic endpoint insertion at a nonreal local saddle

Private written proof, 16 November 2026.

The explicit sharp endpoint baseline has the actual Gamma connection
coefficients, uniformly on each prescribed fixed-height rectangle.
At a genuinely nonreal point the two conjugate modes have unequal
absolute values. This gives a polynomial lower bound, uniformly for
bounded real endpoint parameters including zero, despite their
oscillation in \(\log N\). The exact designated-half representatives
inherit that bound.

The last section applies this insertion to a supplied nonzero local
Gaussian saddle contribution. It neither supplies the geometric cycle
of the original closing nor estimates its other currents.

## 1. Actual normalization and the tall connection formula

Write
\[
 h=N^{-1},\qquad C_N(x)=2\cos(2\pi x+\pi h),\qquad
 w_N(\alpha)=2\cosh(\alpha h),\qquad
 B_N(x,\alpha)=K_N(w_N(\alpha),C_N(x)).
 \tag{1}
\]
The endpoint kernel is the original canonical polynomial. Fix a real
parameter bound \(|\alpha|\le A\), a target \(x_0\in(0,1/2)\), and a
sufficiently small buffered real interval about \(x_0\). Fix arbitrary
finite upper and lower heights. The resulting rectangles, including
all buffers below, have real parts strictly between \(0\) and \(1/2\).

Let \(V_N\) be the particular two-value-normalized baseline of the
reflected sharp connection theorem. Thus its cutoff, mode pair and
actual physical anchor are fixed as in that theorem. In particular,
at a physical anchor \(x_{j_*}=j_*/N\) in its fixed right buffer,
\[
 V_N(x_{j_*})=B_N(x_{j_*}),\qquad
 V_N(x_{j_*}-h)=B_N(x_{j_*}-h).
 \tag{2}
\]
The anchor remains a fixed distance from both endpoints and the fold.
No arbitrary homogeneous solution is added to this normalization.

Put
\[
 \nu=\alpha/\pi,\qquad
 \ell(x)=\Log\sin(\pi x),\qquad L_N=\log(N/\pi),\qquad
 S_N(x)=(N/\pi)\sin(\pi x).
 \tag{3}
\]
The logarithm is the continuation of the real logarithm. Indeed,
\(\Re\sin(\pi x)>0\) on \(0<\Re x<1/2\), so this logarithm is
single-valued on every rectangle under consideration.

For real \(\nu\ne0\), define
\[
 k_\pm(\nu)=
 \frac{\Gamma(\pm i\nu)}{\Gamma(1/2\pm i\nu/2)^4},\qquad
 C_0(\nu)=k_++k_-,\qquad C_1(\nu)=i\nu(k_+-k_-).
 \tag{4}
\]
The removable values are
\[
 C_0(0)=\frac{2(\gamma_E+4\log2)}{\pi^2},\qquad
 C_1(0)=\frac2{\pi^2}.
 \tag{5}
\]
Use the specified logarithm to set
\[
 g_\alpha(S_N(x))=
 \frac1{S_N(x)}
 \left\{C_0(\nu)\cos(\nu(L_N+\ell(x)))
       +C_1(\nu)\frac{\sin(\nu(L_N+\ell(x)))}{\nu}\right\}.
 \tag{6}
\]
The sine quotient is removable at zero. For nonzero real \(\nu\),
this is equivalently
\[
 g_\alpha(S_N(x))
   =k_+S_N(x)^{-1+i\nu}+k_-S_N(x)^{-1-i\nu}.
 \tag{7}
\]

**Theorem 1.** On every smaller buffered rectangle of the prescribed
fixed height there is \(\epsilon_0>0\) such that, for every fixed
spatial derivative order \(k\),
\[
 \partial_x^k V_N(x,\alpha)=
 \partial_x^k g_\alpha(S_N(x))+O_k(N^{-1-\epsilon_0}).
 \tag{8}
\]
Constants are uniform for real \(|\alpha|\le A\), at both parities
of \(N\), and also for \(N\)-dependent real parameters in this compact
interval. The exponent does not decrease merely because the prescribed
height is larger; the constants and required buffers may depend on it.
No endpoint-parameter derivative version of (8) is asserted.

**Proof.** The archived actual value connection theorem gives, at
the anchor in (2),
\[
 \binom{B_N(x_{j_*})}
       {N(B_N(x_{j_*})-B_N(x_{j_*}-h))}
 =
 \binom{g_\alpha(S_N(x_{j_*}))}
       {\partial_x g_\alpha(S_N(x_{j_*}))}
       +O(N^{-1-\epsilon}).
 \tag{9}
\]
Its error is uniform through the coalescence \(\alpha=0\) and at both
parities. In particular the second entry is an actual two-value
quantity; we have not replaced an independent spectral normal by
a derivative.

Let \(H_{0,N},H_{1,N}\) be the coalescence-safe mode pair used to
define \(V_N\), and let
\[
 \psi_0(x)=\frac{\cos(\nu\ell(x))}{\sin(\pi x)},\qquad
 \psi_1(x)=\frac{\sin(\nu\ell(x))}{\nu\sin(\pi x)}.
 \tag{10}
\]
The sine-factor estimates in the reflected theorem give
\[
 H_{i,N}=\psi_i+O_{\mathrm{hol},x}(h)
 \tag{11}
\]
on the whole prescribed fixed-height rectangle, uniformly on the real
parameter compact. This follows there from the sharper centered
estimate at \(x+h/2\). The same estimate holds for all fixed spatial
derivatives on buffered rectangles. Consequently the balanced frame
\[
 \mathcal Y_N(x)=
 \begin{pmatrix}
 H_{0,N}(x)&H_{1,N}(x)\\
 [H_{0,N}(x)-H_{0,N}(x-h)]/h&
 [H_{1,N}(x)-H_{1,N}(x-h)]/h
 \end{pmatrix}
 =
 \begin{pmatrix}\psi_0&\psi_1\\\psi_0'&\psi_1'\end{pmatrix}
       +O(h)
 \tag{12}
\]
is uniformly invertible at the real anchor. The limiting determinant
is \(\pi\cos(\pi x)/\sin^3(\pi x)\), independently of \(\nu\).
The divided-color frame in the reflected theorem and (12) are related
at the anchor by an invertible row scaling; hence they define exactly
the same coefficient vector \(\mathbf a_N\) for \(V_N\).

Define the explicit leading coefficients
\[
 a_{0,N}^{\,0}=\frac{\pi}{N}
 \left\{C_0\cos(\nu L_N)+C_1\frac{\sin(\nu L_N)}{\nu}\right\},
 \qquad
 a_{1,N}^{\,0}=\frac{\pi}{N}
 \left\{-\nu C_0\sin(\nu L_N)+C_1\cos(\nu L_N)\right\}.
 \tag{13}
\]
The addition formulas give exactly
\[
 (\psi_0,\psi_1)\mathbf a_N^{\,0}=g_\alpha(S_N(x)),\qquad
 (\psi_0',\psi_1')\mathbf a_N^{\,0}=\partial_x g_\alpha(S_N(x)).
 \tag{14}
\]
Uniformly on the real parameter compact,
\[
        c/N\le|\mathbf a_N^{\,0}|\le C(1+\log N)/N.
 \tag{15}
\]
Here \(|\sin(\nu L_N)/\nu|\le L_N\), including its value at zero.
For the lower bound at nonzero real \(\nu\), the two entries of
\(N\mathbf a_N^{\,0}/\pi\) are
\(2\Re(k_+e^{i\nu L_N})\) and
\(-2\nu\Im(k_+e^{i\nu L_N})\). Their Euclidean norm is at least
\(2|k_+|\min(1,|\nu|)\), uniformly bounded below on the real
compact because the Gamma function has no zeros and
\(|\nu k_+|\to1/\pi^2\). At zero the second entry is \(C_1(0)\).
Combining (9), (12) and (14) proves
\[
 \mathbf a_N-\mathbf a_N^{\,0}
   =O(N^{-1-\epsilon})+O((1+\log N)/N^2)
   =O(N^{-1-\epsilon_0}),
 \tag{16}
\]
where one may take \(\epsilon_0=\min(\epsilon,1/2)\).
In particular this is also a relative vector estimate
\(|\mathbf a_N-\mathbf a_N^{\,0}|/|\mathbf a_N^{\,0}|
=O(N^{-\epsilon_0})\); no lower bound for either separate
coalesced coordinate is required.
Multiplying these coefficients by the bounded explicit modes and
using (11) proves (8), including its derivatives. This proof transports
two actual coefficients in an explicit global mode frame; it is not
analytic continuation of a small real-axis error. \(\square\)

## 2. A uniform nonreal lower bound

Let \(\mathcal K\) be a compact subset of the prescribed rectangle
with \(\Im x\ne0\), and reserve a slightly larger such compact
neighborhood. Then
\[
 \beta(x):=\Im\ell(x),\qquad
                 \inf_{x\in\mathcal K}|\beta(x)|=\beta_0>0.
 \tag{17}
\]
Indeed, for \(x=a+iy\) in this strip,
\(\Im\sin(\pi x)=\cos(\pi a)\sinh(\pi y)\), which is nonzero
exactly when \(y\ne0\).

**Theorem 2.** For all sufficiently large \(N\), uniformly for
\(x\in\mathcal K\) and real \(|\alpha|\le A\),
\[
 \frac{c}{N}\le |V_N(x,\alpha)|\le\frac{C(1+\log N)}N.
 \tag{18}
\]
Every fixed spatial derivative has the upper bound
\(C_k(1+\log N)/N\). Moreover
\[
 \frac{V_N(x,\alpha)}{g_\alpha(S_N(x))}
                         =1+O(N^{-\epsilon_0}).
 \tag{19}
\]
The denominator is nonzero throughout this compact neighborhood.

**Proof.** For real \(\nu\ne0\), \(k_-=\overline{k_+}\).
The reverse triangle inequality in (7), with
\(\Log S_N=L_N+\ell(x)\), gives
\[
 |g_\alpha(S_N(x))|
 \ge \frac{2\pi |k_+(\nu)|}{N|\sin(\pi x)|}
                          |\sinh(\nu\beta(x))|.
 \tag{20}
\]
This inequality eliminates the phase \(e^{i\nu\log(N/\pi)}\).
The Gamma function is nonzero, and its expansion at zero gives
\[
                |\nu|\,|k_+(\nu)|\longrightarrow1/\pi^2.
 \tag{21}
\]
Thus the right side of \(N\) times (20) has the strictly positive
continuous limit
\[
                        \frac{2|\beta(x)|}{\pi|\sin(\pi x)|}.
 \tag{22}
\]
At zero itself, (5)--(6) give
\[
 g_0(S_N(x))=
 \frac{2}{\pi N\sin(\pi x)}
       \{\log(N/\pi)+\ell(x)+\gamma_E+4\log2\}.
 \tag{23}
\]
The imaginary part of the expression in braces proves the lower
bound (22) directly. Compactness therefore makes (20)--(23) uniform
for the entire real parameter interval, including sequences
\(\alpha=\alpha_N\to0\). This proves \(|g_\alpha|\ge c_0/N\).

The coalescence-safe formula (6) and its fixed spatial derivatives
are bounded by \(C_k(1+\log N)/N\); the real parameter restriction
prevents growth of its \(L_N\)-dependent oscillations. Now (8)
proves (18)--(19) and the derivative assertions. \(\square\)

The restriction to a nonreal compact is essential to this argument.
No lower bound is asserted on the real interval, where the two
conjugate terms may interfere with equal absolute values.

## 3. Exact physical representatives and shared insertions

Choose either sign \(\sigma\in\{+1,-1\}\). Use the sharp one-sided
assembly on the same window, with any fixed positive error rate
\(\gamma\) below its local sharp rate. It gives
\[
                  H_N^\sigma=V_N+C_N^\sigma
 \tag{24}
\]
with exactly the original physical values and first spectral normals,
and, for every fixed spatial derivative,
\[
 |\partial_x^k C_N^\sigma|\le C N^p e^{-N\gamma}
                         \quad\text{when }\sigma\Im x\ge0.
 \tag{25}
\]
Therefore (8), (18) and (19) also hold with \(H_N^\sigma\) in
place of \(V_N\) on every nonreal compact in its designated half.
This is a lower bound for an exact local full-jet representative,
not for the canonical polynomial evaluated away from its physical
nodes. Nor is it a lower bound for its original closed trace.

For a fixed number \(r\) of factors, let \(x_i(z)\) be fixed
holomorphic functions near a point \(z_*\in\mathbb C^d\). Require that
their images of a common compact neighborhood lie in the designated
nonreal compacts just described. Let all \(\alpha_i\) be real and
bounded, and set
\[
                    \mathcal B_N(z)=
           \prod_{i=1}^r H_{i,N}^{\sigma_i}(x_i(z),\alpha_i).
 \tag{26}
\]
Then uniformly on a smaller neighborhood,
\[
 |\mathcal B_N(z_*)|\ge cN^{-r},\qquad
 |\partial_z^\lambda\mathcal B_N(z)|
              \le C_\lambda\left(\frac{1+\log N}{N}\right)^r.
 \tag{27}
\]
The same statement holds with any or all factors replaced by their
baselines. It follows directly from the product and chain rules.
Repeated/shared colors are allowed: their physical first normals
are retained by the ordinary product rule, not independent sampling.
Endpoint-parameter derivatives or normal derivatives of the insertion
are not asserted to have a nonzero lower bound.

## 4. Conditional local stationary-phase consequence

The following hypotheses describe an already supplied local saddle
contribution. They are not conclusions about the original global
integration cycle.

Let \(\Gamma_{\mathrm{loc}}\) have a fixed real \(d\)-dimensional
parameterization \(z=z(u)\), with \(z(0)=z_*\) and
\(|z(u)-z_*|\le C|u|\), contained in the neighborhood of (27).
Suppose its bare amplitude and integration density satisfy a uniform
absolute bound \(|a_N(z(u))\,d\mu|\le C\,du\), and its phase obeys
\[
       \Re(\Phi(z(u))-\Phi(z_*))\le-c|u|^2.
 \tag{28}
\]
Suppose the bare local integral has its specified nonzero asymptotic
\[
 I_N^0:=\int_{\Gamma_{\mathrm{loc}}}e^{N\Phi(z)}a_N(z)\,d\mu
 =e^{N\Phi(z_*)}N^{-d/2}\{A_*+o(1)\},\qquad A_*\ne0.
 \tag{29}
\]
Uniform versions use uniform constants in (27)--(29) and
\(\inf|A_*|>0\). A common scalar carrier may be factored out of both
integrals without changing the assertion.

**Corollary.** Under these supplied local hypotheses,
\[
 \int_{\Gamma_{\mathrm{loc}}}e^{N\Phi(z)}
                  a_N(z)\mathcal B_N(z)\,d\mu
 =\mathcal B_N(z_*)\,e^{N\Phi(z_*)}N^{-d/2}
                                      \{A_*+o(1)\}.
 \tag{30}
\]
In particular the endpoint insertion does not annihilate this
already specified nonzero local coefficient, even when its own
coefficient oscillates in \(\log N\).

**Proof.** By (27) and the mean-value estimate along short paths in
the fixed neighborhood,
\[
 |\mathcal B_N(z(u))-\mathcal B_N(z_*)|
       \le C|u|\left(\frac{1+\log N}{N}\right)^r.
 \tag{31}
\]
Equations (28) and the absolute amplitude bound show that subtracting
\(\mathcal B_N(z_*)I_N^0\) from the integral in (30) has modulus at most
\[
 C e^{N\Re\Phi(z_*)}N^{-(d+1)/2}
                         \left(\frac{1+\log N}{N}\right)^r.
 \tag{32}
\]
After division by
\(|\mathcal B_N(z_*)e^{N\Phi(z_*)}N^{-d/2}|\), this is
\(O((1+\log N)^r/\sqrt N)=o(1)\), by (27). Equation (29)
proves (30). \(\square\)

The exact one-sided trace construction still retains its real
interface, both exterior half-contours, their vertical sides,
all grid aliases, the original crossing, all shared spectators,
and all physical rows outside the window. Nothing in (30) estimates
these other terms or rules out cancellation between distinct local
cycles in their closing. In particular it does not identify the
original geometric cycle coefficient or prove a whole-source lower
bound or a parent-volume comparison.

## 5. Coverage and direct sources

The earlier
[fixed-strip endpoint asymptotics](research_endpoint_fixed_strip_asymptotics.md)
already continue the connection formula to a narrow strip and prove
a local multiplier consequence for parameters of size \(1/\log N\).
That coverage is not used as a proof dependency here. The new point
is the actual two-coefficient transport in the explicit tall mode
frame, followed by the nonreal reverse-triangle estimate uniformly
for all bounded real parameters. The local Gaussian comparison above
is included in full to specify the remaining cycle hypothesis.

All three complete direct sources were read at these matching final
pins, and the directly used anchor, uniform coalescence, physical
normal and repair implications were checked:

* [Actual value connection and growing overlap](research_endpoint_value_connection_and_overlap.md),
  SHA256 87801bd8baca255a86fdbcd5170662fd9f2b366f983507f776d5676fd8a324da.
* [Reflected sharp full-normal connection](research_reflected_endpoint_sharp_normal_connection.md),
  SHA256 a8a379d7b492d7d2487de3c1397408478f66242f153ac0cab8eb3d224f226916.
* [Sharp one-sided physical-window assembly](research_sharp_endpoint_one_sided_window_assembly.md),
  SHA256 163d4cf2fc98648c0739152dbb463f2ad8f19d58b34b31d9184469847e60e541.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Existing adopted and public notes are unchanged.
