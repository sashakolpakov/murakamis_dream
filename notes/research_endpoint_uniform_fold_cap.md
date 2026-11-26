# A uniform full-normal fold cap and its actual patch join

Private written proof, 16 November 2026.

The sharp modes extend through the negative spectral endpoint in their
regular divided-color frame. A fold anchor and a reflected full angular
window retain the odd simple value and the even last normal with the
correct trace multiplicity. Weighting the exact Hermite repair by its
analytic error action prevents a quadratic loss across the window.

The resulting error and joining budgets are
\(\mathcal I_2+O(T^4)\) for fold width \(T\). They give a strict
terminal-action margin for every fixed \(|n|\ge3\), and an upper
rate \(\mathcal I_2\) at width \(O(N^{-1/4})\). The latter does not
settle the critical two-power coefficient. Baseline boundary currents
are explicitly retained until they are joined.

## 1. Source, fold modes, and normalization

Put
\[
 h=N^{-1},\quad D=N-1,\quad \eta=(-1)^D,\quad
 C_N(x)=2\cos(2\pi x+\pi h),\quad
 t=\pi-2\pi x-\pi h,\quad w_N(\alpha)=2\cosh(\alpha h).
 \tag{1}
\]
The original kernel is \(K_N(C,Z)=\sum_{k=0}^{D}e_k(C)e_k(Z)\), with
\[
 c_j=2\cos((2j+1)\pi/N),\qquad S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),
 \qquad e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C).
\]
Fix \(r\in\mathbb Z_{\ge0}\), a bounded complex parameter set,
and an integer \(n\).
The actual insertion and outgoing source are
\[
 B_N(C)=\prod_{i=1}^rK_N(w_N(\alpha_i),C),\qquad
 \phi_N[R_N^n B_N K_N(\cdot,Z)].
 \tag{2}
\]
Every output derivative below is a fixed ordinary
\(\partial_Z^q\) at \(Z=-2\); the real-output bounds used in the
proof also retain the whole interval \([-2,2]\).
Fixed endpoint-parameter derivatives are included, with polynomial
losses. All traced first normals remain part of the original trace.

Use the fold cutoff
\[
 \delta_f=\tfrac14,\qquad m_f=\lfloor N/4\rfloor,\qquad
 I_\delta(X)=\int_0^\delta
       \log\frac{\sin^2(\pi X)-\sin^2(\pi v)}
                     {\sin^2(\pi v)}\,dv.
 \tag{3}
\]
The analytic continuation on a fixed rectangle with
\(\delta<\Re X<1-\delta\) uses the sum of the logarithms of
\(\sin\pi(X-v)\) and \(\sin\pi(X+v)\), real on the real interval.
In particular it has no zero or logarithmic ambiguity there.
On this rectangle,
\[
                 \Re I_\delta(X+iY)\ge I_\delta(X).
 \tag{4}
\]
Indeed
\[
 |\sin\pi(X-v+iY)\sin\pi(X+v+iY)|
       \ge \sin^2(\pi X)-\sin^2(\pi v)>0.
 \]

For each parameter chart use the modes in the local atlas, with
cutoff \(m_f\), the same factorial normalization, and the same
resonance subtractions. Before regularization they are
\[
 F_z(x)=4^{-z}\frac{G_N(Nx+z)}{G_N(Nx-z)},\quad
 U_m(z,x)=\sum_{k=0}^{m}a_k(z)F_{z-k}(x),\quad
 \frac{a_k}{a_{k-1}}=\frac{s_{z-k+1}^4}{4s_ks_{2z+1-k}},
 \quad z_\pm=-\tfrac12\pm\frac{i\alpha}{2\pi}.
 \tag{5}
\]
Here \(G_N\) is the specified Gamma-product factorial in the pinned
factorial source, \(a_0=1\), and \(s_z=2\sin(\pi hz)\).
At zero parameter use the coalesced
pair; at an even index resonance use the atlas's reflected tail
subtraction, with its specified fixed cutoff shift.

All its proofs apply uniformly on a fixed symmetric neighborhood of
\(x=1/2\), at any prescribed finite imaginary heights. To check the
endpoint of the cutoff range explicitly, choose a fixed \(a>1/4\)
close enough to \(1/2\) that \(I_{1/4}(a)>0\). Every growing factorial
argument has scaled real part in
\((a-1/4,1-a+1/4)\Subset(0,1)\). The summand product estimate,
initial contraction, and centered \(O_{\rm hol}(h^2)\) mode expansion
are therefore unchanged at \(\delta=1/4\). For fixed \(X\) in this
neighborhood, \(I_v(X)\) first increases and then decreases in \(v\);
its endpoint values at \(0,1/4\) are nonnegative. This is precisely
the positivity used in the finite-sum proof. The same observations
work uniformly for all cutoffs \(\delta\) in a sufficiently small
fixed interval \([\delta_0,1/4]\).

Write \(H=(H_0,H_1)\) for the chart's scalar mode row, and
\[
 \mathcal V_f(x)=
 \binom{f(x)}{[f(x)-f(x-h)]/[C_N(x)-C_N(x-h)]},\qquad
 \mathcal F(x)=(\mathcal V_{H_0},\mathcal V_{H_1}).
 \tag{6}
\]
These quotients have their regular spectral divided-difference
meaning at coincident colors. The centered limiting spectral
Wronskians in the reflected theorem and parameter atlas are units
at \(C=-2\). Hence \(\mathcal F,\mathcal F^{-1}\), and every fixed
derivative are uniformly bounded on a fixed neighborhood through
the fold, uniformly for \(\delta\in[\delta_0,1/4]\).

Choose the physical anchor
\[
 j_*=\begin{cases}N/2-1,&N\text{ even},\\(N-1)/2,&N\text{ odd}.
 \end{cases}
 \quad
 \mathbf a_*=\mathcal F(j_*h)^{-1}
       \mathcal V_{K_N(w_N,C_N(\cdot))}(j_*h),\qquad
 V_N(x)=H(x)\mathbf a_*.
 \tag{7}
\]
For all large levels the two colors in (7) are distinct. Their
separation is of order \(h^2\), but the actual polynomial divided
difference has polynomial norm by the endpoint bound and Markov.
Thus the anchor is holomorphic in the local parameter chart with
polynomial norm. This is an actual two-value normalization; no new
normal is prescribed at the odd simple node.

**Fold connection.** Uniformly at every physical row in the fixed
symmetric neighborhood, at both parities,
\[
 |u_N(x_j)-V_N(x_j)|+|u_N'(x_j)-V_N'(x_j)|
       \le CN^p e^{-NI_\delta(x_j)},\qquad
 u_N(x)=K_N(w_N,C_N(x)).
 \tag{8}
\]
The same bound holds for fixed parameter derivatives. On fixed-height
rectangles the baseline is polynomially bounded.

For clarity, the regular-frame proof supplies this stronger placement,
not just a limit of fixed windows. Define
\(\mathbf a_N(x)=\mathcal F(x)^{-1}\mathcal V_{u_N}(x)\).
The ordinary operator and its original source are
\[
 \mathscr J_N f=(c_0+A_N+B_N)f-A_Nf(x+h)-B_Nf(x-h),\quad
 A_N=\frac{s_{Nx+1}^4}{s_{2Nx+1}s_{2Nx+2}},\quad
 B_N=\frac{s_{Nx}^4}{s_{2Nx}s_{2Nx+1}},\quad c_0=2\cos(\pi h),
\]
\[
 r_K=(\mathscr J_N-w_N)u_N
   =-\frac{P_N(w_N)P_N(C_N(x))}{N^4(C_N(x)-c_0)},\qquad
 P_N(C)=2T_N(C/2)+2,\quad P_N(C_N(x))=4\sin^2(\pi Nx).
\]
Here \(T_N\) is the Chebyshev polynomial. The apparent angular poles
are canceled in the regular frame. Its exact coefficient equations are
\[
 \mathbf a_N(x+h)=(I+M_N(x))\mathbf a_N(x)-\ell_N(x)r_K(x),
 \quad
 \|M_N\|+\|M_N'\|\le CN^p e^{-NI_\delta(\Re x)},
 \tag{9}
\]
where \(r_K=r_K'=0\) at all physical rows and
\(\mathbf a_N(1-x)=\mathbf a_N(x)\).
Propagation from \(j\) to \(N-j\), followed by the differentiated
reflection, gives
\[
 (I+P_j)\mathbf a_N'(x_j)=-Q_j\mathbf a_N(x_j),\qquad
 \|P_j-I\|+\|Q_j\|\le CN^p e^{-NI_\delta(x_j)}.
 \tag{10}
\]
This is uniform to the fold: \(I_\delta\) is symmetric and has its
minimum at the ends of that propagation interval, and the frame has
no angular singularity. At the coincident row \(j=N/2\), reflection
itself gives \(\mathbf a_N'=0\). Propagating the value equation to
(7), or first reflecting it, proves the value part of (8). The
anchor is within \(O(h)\) of \(1/2\); the harmless possible loss
in \(NI_\delta\) is bounded. Differentiating \(u_N=H\mathbf a_N\)
then proves the derivative part. This repeats the exact source
argument without dividing by a vanishing angular derivative.

At odd levels the central angular derivative is zero by scalar
reflection and only the simple spectral value is used. At even
levels the last two angular lifts represent one double spectral
root; its actual first normal is retained. In angular coordinates
\(C_N'\asymp h\) there, so conversion of (8) to its spectral
normal costs only a power of \(N\).

## 2. A pointwise weighted repair on a mirrored cap

Choose integers \(j_L,j_R\) with
\[
 j_R=N-1-j_L,\qquad
 a_N=(j_L-\tfrac12)h,\quad b_N=(j_R+\tfrac12)h,\quad
 T_N=\pi-2\pi j_L/N.
 \tag{11}
\]
The angular cap is \([-T_N,T_N]\); its physical rows are
\(j_L\le j\le j_R\). A fixed cap, or a shrinking cap
\(T_N\asymp N^{-1/4}\), fits in the fixed neighborhood above.
All constants below are uniform over these choices.

Use the centered analytic error weight
\[
 E_{\delta,N}(x)=\exp[-NI_\delta(x+h/2)].
 \tag{12}
\]
It is a unit and has the exact scalar reflection
\(E_{\delta,N}(1-h-x)=E_{\delta,N}(x)\).
Replacing \(I_\delta(x_j)\) in (8) by
\(I_\delta(x_j+h/2)\) costs a bounded factor. Define normalized
error data for each inserted factor by
\[
 \widetilde e_j=\frac{u_N(x_j)-V_N(x_j)}{E_{\delta,N}(x_j)},\qquad
 \widetilde d_j=
 \frac{u_N'(x_j)-V_N'(x_j)
       -(E_{\delta,N}'/E_{\delta,N})(x_j)
                     [u_N(x_j)-V_N(x_j)]}{E_{\delta,N}(x_j)}.
 \tag{13}
\]
They and their fixed parameter derivatives have polynomial bounds.
With \(\kappa_h=2\pi/h\), set
\[
 \widetilde C^\sigma(x)=
 \sum_{j=j_L}^{j_R}
 [\widetilde e_j+
      (\widetilde d_j-\sigma i\kappa_h\widetilde e_j)(x-x_j)]
 e^{\sigma i\kappa_h(x-x_j)}
                 \operatorname{sinc}^2((x-x_j)/h),
 \quad
 H^\sigma=V_N+E_{\delta,N}\widetilde C^\sigma.
 \tag{14}
\]
This preserves both original angular jets exactly. At the odd
central node it imposes the original zero angular derivative, not
an additional spectral normal.

The normalized repairs have polynomial norm, with polynomial fixed
derivatives, throughout their designated half-rectangles
\(\sigma\Im x\ge0\). Thus (4) gives the pointwise estimate
\[
 |H^\sigma-V_N|
   \le CN^p e^{-N\Re I_\delta(x+h/2)}
   \le CN^p e^{-NI_\delta(\Re x+h/2)}.
 \tag{15}
\]
The same statement, with polynomial losses, holds for fixed derivatives.
Unlike a repair using the minimum error rate over its whole window,
(15) retains the spatial action at the observation point.

Put \(D_h(x)=(\pi/h)^2\csc^2(\pi x/h)\). Its exact removable
interface is \(E_{\delta,N}(x)\) times
\[
 \sum_j\frac{
 [\widetilde e_j+(\widetilde d_j-i\kappa_h\widetilde e_j)z]
                                      e^{i\kappa_hz}
 -
 [\widetilde e_j+(\widetilde d_j+i\kappa_h\widetilde e_j)z]
                                      e^{-i\kappa_hz}}{z^2},
 \qquad z=x-x_j.
 \tag{16}
\]
The elementary small-\(z\) Taylor bound and large-\(z\) direct bound
from the repair theorem imply
\[
 |D_h(H^+-H^-)(x)|\le CN^p e^{-NI_\delta(x+h/2)}
                                      \quad(x\text{ real}).
 \tag{17}
\]
Fixed products use \(P^\sigma=\prod_iH_i^\sigma\) and
\(P^0=\prod_iV_i\). Telescoping preserves (15) and (17) with
the same action, not \(r\) times that action, and preserves the
full shared first normal.

The repair has exact reflection
\(H^+(1-h-x)=H^-(x)\). Indeed its mirrored data have equal values
and opposite derivatives, and (14) transforms term by term.
Consequently \(P^+-P^-\) is odd in the angular variable \(t\).
At the odd central physical node its angular derivative is also zero,
since both representatives have the same original angular jet.
Therefore
\[
            D_h(x)\sin t\,[P^+(x)-P^-(x)]
                  \quad\text{has a double zero at }t=0
 \tag{18}
\]
at both parities. At odd levels \(D_h\) has a double pole and the
odd difference begins at order three; at even levels \(D_h\) is
regular at the central midpoint. This is an exact zero statement,
not a uniform small bound on its second derivative.

## 3. Exact cap trace and its normalization

Let \(\phi_{\rm cap}\) mean the original restricted physical trace,
including a double root once and the odd simple root if present.
For any original spectral source \(f\), set
\(g(x)=\sin(2\pi x+\pi h)f(C_N(x))\). Then
\[
 g'(x_j)=-\pi\{(4-c_j^2)f'(c_j)-c_jf(c_j)\},\qquad
 \phi_{\rm cap}(f)=-\frac{\eta}{2\pi}
                              \sum_{j=j_L}^{j_R}g'(x_j).
 \tag{19}
\]
Each double spectral root has two mirrored lifts in this sum.
At odd \(N\), the center has \(g'=-2\pi f(-2)\) and
\(\eta=1\), so it contributes exactly \(f(-2)\).
This verifies the simple-node coefficient separately.

Retain the original crossing carrier
\[
 \mathfrak c_{N,n}=e^{\pi i nD^2/(4N)},\qquad
 E_{N,n}(x)=\mathfrak c_{N,n}e^{inNt^2/(4\pi)}.
 \tag{20}
\]
For an outgoing spectator \(A_N(C;Z)\), define
\[
 g_\sigma(x)=\sin t\,P^\sigma(x)E_{N,n}(x)A_N(C_N(x);Z).
 \tag{21}
\]
With both exterior half-contours and all their vertical sides,
the exact cap identity is
\[
 \boxed{\quad
 \phi_{\rm cap}[R_N^n B_N A_N]
 =-\frac{\eta}{4\pi^2i}
 \left\{\int_{E_-}D_hg_-\,dx+\int_{E_+}D_hg_+\,dx
                  +\int_{a_N}^{b_N}D_h(g_+-g_-)\,dx\right\}.
 \quad} \tag{22}
\]
The prefactor is half the positive-lift-only window prefactor.
It follows from (19) and the double-pole residue of \(D_h\).
No angular mirror is counted twice after this factor.
The formula is coefficientwise in shared colors before other traces.

As in the compact-interface theorem, split the actual outgoing kernel
into \(K_N^<=\sum_{k<\lfloor N/2\rfloor}e_k(C)e_k(Z)\) and its
entire remaining sector. The latter's restricted physical trace,
including all fixed output normals and microscopic products, is
polynomially bounded, term by term. This follows from its polynomial
real norms, Markov, and the original full trace, and includes the
extra odd middle row. It is retained as a separate source.
Use (22) with \(A_N=K_N^<\) on the deformed contours.

## 4. Exact half-plane prefactors and the fold action

There is no exponential tolerance in the needed fold kernel bound.
On every fixed compact set \(\mathcal C\Subset\{\Re C<2\}\), the
all-row logarithmic estimate in the first-short source is
\[
 \log F_{j,N}(C)=N\Psi_{j/N}(C)+O(\log N),\qquad
                    \Re\Psi_{j/N}(C)\le\Re\Psi_{1/2}(C).
 \tag{23}
\]
Its exact interpolation of \(K_N^<\) at the double physical nodes
has polynomial real cardinal norm at both parities. Therefore
\[
 \sup_{Z\in[-2,2]}|K_N^<(C,Z)|
                    \le CN^p e^{N\Re\Psi_{1/2}(C)}.
 \tag{24}
\]
Apply Markov in \(Z\), and Cauchy to the normalized holomorphic
function on a larger half-plane compact, to retain every fixed
ordinary derivative. This uses the \(O(\log N)\) half-plane result,
not the weaker \(o(N)\) continuation on the whole slit plane.
For bounded heights and sufficiently small \(|\Re t|\),
\(C=-2\cos t\) lies in such a compact and
\(\Psi_{1/2}(C)=\psi(t,0)\).

Write
\[
 G=\int_0^{\pi/4}\log\cot v\,dv,\qquad \mathcal I_2=2G/\pi,\qquad
 \mathcal J(t)=I_{1/4}\!\left(\frac{\pi-t}{2\pi}\right).
 \tag{25}
\]
The fixed-cutoff action has the exact analytic expression
\[
 \mathcal J(t)=\mathcal I_2+
 \frac1\pi\int_0^{\pi/4}
             \log(1-\sin^2(t/2)\sec^2v)\,dv.
 \tag{26}
\]
The value at zero is the calibrated \(I_{1/4}(1/2)=\mathcal I_2\).
Expanding (26), using
\(\int_0^{\pi/4}\sec^2v\,dv=1\) and
\(\int_0^{\pi/4}\sec^4v\,dv=4/3\), gives
\[
 \mathcal J(t)=\mathcal I_2-\frac{t^2}{4\pi}
                          -\frac{t^4}{48\pi}+O(t^6).
 \tag{27}
\]
The calibrated derivative
\(\psi'(t)=-\operatorname{asinh}(\tan(t/2))/\pi\) gives
\[
 \psi(t,0)=2\mathcal I_2-\frac{t^2}{4\pi}
                          -\frac{t^4}{192\pi}+O(t^6),
 \qquad
 \psi(t,0)-\mathcal J(t)
             =\mathcal I_2+\frac{t^4}{64\pi}+O(t^6).
 \tag{28}
\]
The positive quartic sign is essential. A single fold cutoff is
not the separately optimized cutoff at nonzero \(t\).

Equations (17), (21), and (24) prove the real-interface bound
\[
 |\partial_Z^q\,{\rm Interface}_{\rm cap}(-2)|
                  \le CN^p e^{N(\mathcal I_2+C T_N^4)}.
 \tag{29}
\]
The original crossing is unit-modulus on the real path.
Fixed parameter derivatives have the same form.

There is also a uniform vertical improvement. At \(t=-iH\),
\[
 \frac{d}{dH}\psi(-iH,0)=
       \frac{\arcsin(\tanh(H/2))}{\pi},\qquad
 \frac{d}{dH}\mathcal J(-iH)=
       \frac{\arctan(\tanh(H/2))}{\pi}.
 \tag{30}
\]
For the second identity, substitute \(\tan v=y\) in the derivative
of (26). Hence
\[
 \frac{d}{dH}\{\psi(-iH,0)-\mathcal J(-iH)-H\}
                                                     \le-\tfrac34.
 \tag{31}
\]
The difference \(\arcsin p-\arctan p\) increases from zero to
\(\pi/4\) on \(0\le p\le1\), which proves the constant.

At either midpoint side the exact grid kernel has modulus
\((\pi N)^2\operatorname{sech}^2(NH/2)\le4\pi^2N^2e^{-NH}\).
For the repair corrections the phase is therefore
\[
 \Re[\psi(t-i\sigma H,0)-\mathcal J(t-i\sigma H)]
                    +(\sigma nt/(2\pi)-1)H.
 \tag{32}
\]
On any prescribed finite height interval, continuity in small real
\(t\), (31), and fixed \(n\) make its height derivative at most
\(-1/2\), after reducing a fixed cap width \(T_0>0\).
Thus all error verticals have the bound (29), and error horizontals
at height \(H>0\) improve its exponent by \(H/2\).
The constants are uniform for \(T_N\le T_0\).

Baseline horizontals have phase
\(\Re\psi(t-i\sigma H,0)+(\sigma nt/(2\pi)-1)H\).
At \(t=0\), its height derivative is at most \(-1/2\).
Choosing a fixed \(H>2\mathcal I_2\), and then a smaller fixed
\(T_0\), puts both baseline horizontals strictly below
\(\mathcal I_2\).

Let \(\mathcal V^0_{\rm cap}\) denote precisely the four baseline
vertical half-side integrals in (22), with their original prefactor,
using \(P^0=\prod_iV_i\) and \(A_N=K_N^<\). The preceding estimates
prove the concrete retained-boundary statement
\[
 \boxed{\quad
 |\partial_Z^q[
    \phi_{\rm cap}(R_N^n B_N K_N(\cdot,Z))
                          -\mathcal V^0_{\rm cap}(Z)]_{Z=-2}|
             \le CN^p e^{N(\mathcal I_2+C T_N^4)}.
 \quad} \tag{33}
\]
In particular \(T_N\asymp N^{-1/4}\) gives a polynomial times
\(e^{N\mathcal I_2}\). Formula (33) does not bound the unjoined
baseline verticals, whose real endpoints can have the bare edge rate.

## 5. Joining the fold to the compact patches

Use the same factorial, parameter-chart recipe, and physical
divided-color anchor (7) for the adjacent patch. Its cutoff may
be any \(\delta'\in[\delta_0,1/4]\), in particular the optimized
cutoff at the seam. The finite-tail comparison from the compact
theorem is uniform in this closed cutoff range. Every index in the
tail is of order \(N\), all factorial strips have fixed buffers,
and there are at most \(N\) summands. Resonance subtractions have
the same fixed shifts and the same residues on both patches.
Their ordinary mode and frame difference is consequently bounded by
\[
 CN^p e^{-N\min(I_{1/4}(\Re x),I_{\delta'}(\Re x))}.
 \tag{34}
\]
The inverse frames at the common fold anchor are uniformly bounded.
The difference of their normalized coefficients satisfies the same
bound there; monotonicity towards the fold makes its saving at
least the saving at the overlap. This proves (34) for the actual
baselines, not only their residuals.

Use the pointwise weighted repair (12)--(15) with the respective
cutoffs on each patch. On a common designated half, (4) and (34)
give the same difference estimate for the exact representatives,
with the minimum of the two real actions. All constants remain
uniform if the seam width tends to zero and \(\delta'\to1/4\);
no inverse angular Wronskian is used.

For exact bookkeeping, write the adjacent compact block with its
reflected angular block and the half normalization (22). Its sum
is the original positive-lift trace. At a common midpoint the two
baseline vertical currents in (33) combine with the neighboring
ones into the actual difference of representatives. Both sides
have the same normalization and crossing. The estimate is for this
jump, not for either baseline current separately.

For a positive seam angle \(T\), take
\(\delta'=\pi^{-1}\arcsin(\cos(T/2)/\sqrt2)\). Its optimized
action is at least the fold action at that seam. The \(O(h)\)
difference of midpoint coordinates costs only a bounded factor.
At calibrated height \(H_n\), for \(|n|\ge2\), the compact theorem
gives the exact seam phase
\[
 \mathcal P_{n,\sigma}(T,H)
   =\Re\psi(T-i\sigma H,0)+(\sigma nT/(2\pi)-1)H,
 \quad
 \mathcal P_{n,\sigma}(T,H_n)\le\mathcal I_n.
 \tag{35}
\]
It is convex in \(H\). Subtracting the constant saving from (34)
shows that the joined seam is bounded by a polynomial times the
exponential of \(N\) times
\[
 \max\{\mathcal I_2+C T^4,\ \mathcal I_n-c_{\rm seam}\},
 \tag{36}
\]
where \(c_{\rm seam}>0\) is uniform for small \(T\), since the common action
tends to \(\mathcal I_2\). The weighted corrections obey the same
estimate. The fold baseline horizontals at \(H_n\) have a strict
\(\mathcal I_n\) gap for all sufficiently small fixed \(T\): the
calibrated horizontal phase is strictly concave, and its unique
maximum is at a positive angle separated from this cap.

For each fixed \(|n|\ge3\), choose a small fixed \(T\) such that
\(\mathcal I_2+C T^4<\mathcal I_n\), using the strict all-power
action ordering. Then (29), (32), (36) and the baseline horizontal
gap pay the fold cap and its joined seams strictly below
\(\mathcal I_n\). All constants remain uniform on the bounded
microscopic parameter set and under the stated fixed normals.
This supplies the fold part of the compact-current construction;
it does not independently select its original saddle cycle.

For \(|n|=2\), \(T_N\asymp N^{-1/4}\) makes (36) an upper
rate \(\mathcal I_2\), with polynomial prefactor. This does not
prove a negligible error relative to a decorated saddle. Nor does
it supply uniform estimates for an entire growing collection of
additional compact patches outside that shrinking cap.

## 6. Literal last-summand size and the critical limitation

The mode prefactor can be kept explicitly for bounded real \(\alpha\).
Let \(z=-1/2+i\nu/2\), \(\nu=\alpha/\pi\), and \(k/N=v\)
in a fixed neighborhood of \(1/4\). Direct sine-product telescoping
in (5) gives
\[
 a_kF_{z-k}(x)=(-1)^k4^{-z}
 \frac{G_N(-2z-1)}{G_N(-z-1)^4}
 \frac{G_N(k-z-1)^4}{G_N(k)G_N(k-2z-1)}
 \frac{G_N(Nx+z-k)}{G_N(Nx-z+k)}.
 \tag{37}
\]
All fixed arguments in the first quotient remain in the regular
factorial strip. The defining product gives
\(G_N(s)=(2\pi/N)^s\Gamma(s+1)(1+O(N^{-2}))\) for those fixed
arguments. The bulk factorial expansion, including its
\(\sqrt{2N\sin\pi x}\) factor and all fixed shifts, then gives
\[
 a_kF_{z-k}(x)=
 (-1)^k N^{-2z-2}A_z(x,v)e^{-NI_v(x)}(1+O_{\rm hol}(N^{-1})),
 \tag{38}
\]
where all branches continue from the positive real strip and
\[
 A_z(x,v)=
 4^{-z}(2\pi)^{2z+3}\frac{\Gamma(-2z)}{\Gamma(-z)^4}
 (2\sin\pi v)^{-2z-2}
 \sqrt{\frac{\sin\pi(x-v)}{\sin\pi(x+v)}}
 [4\sin\pi(x-v)\sin\pi(x+v)]^z.
 \tag{39}
\]
Here \(J'(u)=\Log(2\sin\pi u)\), \(J(0)=0\), with the factorial
source's branches. The leading exponent follows by differentiating in \(v\):
the derivative of \(2J(v)+J(x-v)-J(x+v)\) is
\(-\partial_v I_v(x)\), and both vanish at \(v=0\).
The amplitude (39) is a uniform unit on the real parameter compact
and fixed spatial buffers. The factor \(N^{-2z-2}\) has modulus
\(N^{-1}\). At \(z=-1/2,x=1/2,v=1/4\), \(A_z=4\).
At \(z=-1/2\), the actual angular fold \(x=(1-h)/2\), and
\(v=m_f/N\), the same amplitude is \(4+O(h)\).

Equation (38) uses the literal \(v=k/N\). Replacing \(v\) by
\(\delta_f\) retains the explicit rounding factor
\(\exp[N(I_{\delta_f}-I_v)]\). At the exact fold optimizer it is
\(1+O(N^{-1})\); on a shrinking cap it is
\(1+O(t^2+N^{-1})\). It must not be omitted from a fixed-window
relative expansion.

Coalescing the two modes at zero introduces at most a \(\log N\)
factor in their residual. The actual leading coefficient vector
has \(a_0=O(\log N/N)\), \(a_1=O(1/N)\), by the connection
calculation in the nonreal insertion theorem. That calculation
also applies to these modes at a fixed nearby real reference row;
their finite-tail estimates and value transport compare its anchor
to (7) with exponentially small error. Thus the single baseline's
ordinary residual has bound
\[
       |(\mathscr J_N-w_N)V_N(x)|
              \le C\frac{1+\log N}{N^2}e^{-NI_{m_f/N}(x)}
 \tag{40}
\]
on real fold buffers, uniformly for bounded real \(\alpha\).
This sharper residual does not by itself give the sharp prefactor
of its integrated interface.

The exact phase marks remain visible in (16) and (20):
\[
                e^{\pm2\pi iNx}=\eta\,e^{\mp iNt}.
 \tag{41}
\]
They cannot be treated as two freely analytic separated sectors.
For example the removable value part of (16) is proportional to
\[
 \frac{\sin(\kappa_hz)-\kappa_hz\cos(\kappa_hz)}{z^2}
                         =\int_0^{\kappa_h}\xi\sin(\xi z)\,d\xi,
 \quad
 \frac{\sin(\kappa_hz)}z=\int_0^{\kappa_h}\cos(\xi z)\,d\xi.
 \tag{42}
\]
The full interface includes frequencies down to zero. Neither
the written unit frequencies, the exact double zero (18), nor
the residual prefactor (40) proves the needed two-power
noncancellation or negligible closing. Such a conclusion requires
additional control of the actual coherent error sequence and
its original closing.

## 7. Complete direct sources and scope

The new steps are the uniform fold anchor, centered analytic error
weight, mirror-counted cap identity, half-plane polynomial
prefactors, and the actual common-anchor fold join. The sharp mode
construction, residue repair, compact seam comparison and terminal
phase calibration are retained from the following complete sources,
read at their final matching pins:

* [Reflected sharp normal connection](research_reflected_endpoint_sharp_normal_connection.md),
  SHA256 a8a379d7b492d7d2487de3c1397408478f66242f153ac0cab8eb3d224f226916.
* [Local parameter atlas](research_endpoint_sharp_local_parameter_atlas.md),
  SHA256 37cbfdab768bad41aa643859a75f9dfeaa5f1db57888ef14f6d5beeb5b29e019.
* [Sharp one-sided repair](research_sharp_endpoint_one_sided_window_assembly.md),
  SHA256 163d4cf2fc98648c0739152dbb463f2ad8f19d58b34b31d9184469847e60e541.
* [Compact interfaces and actual seams](research_sharp_endpoint_compact_interface_and_seams.md),
  SHA256 178e49b99b51fe767bc29ceadafb00159c179cd42f9ba5469921f64a6eabdde9.
* [Physical rows and shortened-edge interpolation](research_mixed_next_first_short_edge_slit_plane_bound.md),
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
* [Specified factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
* [Actual endpoint connection coefficients](research_endpoint_nonreal_insertion_lower_bound.md),
  SHA256 ab3b4687b53c2168d22342c0e822b243a563f716d2a7a0de18d87c372546d7d0.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Existing adopted and public notes are unchanged.
