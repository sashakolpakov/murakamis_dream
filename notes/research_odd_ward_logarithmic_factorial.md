# A logarithmic-factorial representative of the odd Ward correction

The odd-power Ward correction contains the nonscalar element \(T\Pi_0\).
Its canonical polynomial has polynomial size on the real interval,
but the elementary complex extension of that bound has an exponential
bandwidth cost. That cost is unnecessary inside an original trace.

We construct a meromorphic function of the physical angle which has
exactly the same values and first normals as \(T\Pi_0\). It is even,
holomorphic across the whole original physical window, and has only
logarithmic size on every fixed-height rectangle over that window.
On an interior strip its leading term is the nonzero constant
\(2(-1)^N\log N\). The first poles and the exact period defect are
also retained. In particular this representation does not justify
discarding endpoint contributions after an arbitrary window shift.

## 1. The original coupon and the canonical factorial

Put
\[
 N\ge2,\quad D=N-1,\quad \theta=\pi/N,\quad
 \sigma=(-1)^N,\quad z(t)=-2\cos t .
\]
The algebra and trace are the original
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\) and \(\phi_N\).
Let \(\Pi_0\) be the full spectral idempotent at
\(c_0=2\cos\theta\), including its zero first derivative.
Write
\[
                         P_N^{\rm W}=T\Pi_0.
\]
The superscript distinguishes this coupon from the defining Chebyshev
polynomial. The full value and normal formulas proved in
[the signed Ward note](research_signed_gaussian_ward_endpoint_packet.md)
are
\[
 \begin{split}
 P_N^{\rm W}(c_j)
 &=\sigma\left[2\cos\theta+
                    2\sin\theta\sum_{r=1}^j\cot(r\theta)\right],\\
 (P_N^{\rm W})'(c_j)
 &=-\sigma\frac{\sin\theta}{4\sin((2j+1)\theta)}
                      \sum_{r=j+1}^{D-j}\csc^2(r\theta).
 \end{split}                                             \tag{1}
\]
The normal formula concerns the distinct double nodes. At the odd
simple node \(z=-2\), only the value is prescribed.

Let \(G_N\) be the original canonical factorial, \(G_N(0)=1\), and
\(g_N=\log G_N\) on its nonzero strip. We use only its already proved
exact derivative and recurrence:
\[
 g_N'(z)=\frac{\pi}{N^2}\sum_{k=0}^{D}
                  (z-k)\cot\frac{\pi(z-k)}N,             \tag{2}
\]
\[
 g_N'(z+1)-g_N'(z)=\theta\cot(\theta(z+1)).
                                                               \tag{3}
\]
Terms at \(z=k\) in (2) have their removable values.
These identities are proved directly from the defining gamma product
in [the exact factorial note](research_exact_cyclotomic_factorial.md).

Define
\[
 \ell_N(t)=\frac D2-\frac{t}{2\theta},\qquad
 \boxed{\displaystyle
 V_N(t)=\sigma\left[
 2\cos\theta+
 \frac{2\sin\theta}{\theta}
             \{g_N'(\ell_N(t))-g_N'(0)\}\right].}        \tag{4}
\]

## 2. Exact equality of all physical Hermite data

**Theorem 1.** The function \(V_N\) is even and holomorphic on
\[
                       |\Re t|<\pi+\pi/N.              \tag{5}
\]
At every physical angle
\(\tau_j=(D-2j)\theta\), it has exactly the value and required
first normal of \(P_N^{\rm W}(-2\cos t)\). Consequently (4)
may replace that coupon inside any original trace, with arbitrary
polynomial spectators and free boundary variables retained.

**Proof.** The finite sum (2) is invariant under
\(z\mapsto D-z\): reindex \(k\mapsto D-k\), and use the
evenness of \(w\cot(\pi w/N)\). Hence
\[
                g_N'(D-z)=g_N'(z),\qquad
                g_N''(D-z)=-g_N''(z).                   \tag{6}
\]
This proves that (4) is even. The nonzero factorial strip
\(-1<\Re z<N\) becomes exactly (5), so it is holomorphic there.

At \(t=\tau_j\), \(\ell_N(t)=j\), and (3) gives
\[
 g_N'(j)-g_N'(0)=\theta\sum_{r=1}^j\cot(r\theta).
\]
Substitution into (4) proves the value formula in (1).
Differentiate (3):
\[
                  g_N''(z+1)-g_N''(z)
                              =-\theta^2\csc^2(\theta(z+1)).
\]
For a double node represented by \(j<D/2\), sum this identity
from \(j\) to \(D-j\), and use (6). It gives
\[
                  g_N''(j)=\frac{\theta^2}{2}
                           \sum_{r=j+1}^{D-j}\csc^2(r\theta).
\]
Therefore
\[
 V_N'(\tau_j)=-\sigma\frac{\sin\theta}{2}
                              \sum_{r=j+1}^{D-j}\csc^2(r\theta).
                                                               \tag{7}
\]
Division by \(dz/dt=2\sin\tau_j
=2\sin((2j+1)\theta)\) yields precisely the normal in (1).
The negative physical angle gives the same spectral derivative by
evenness. At the odd simple node \(t=0\), the value is the one
already checked; no additional normal is required.

The original trace is determined by these values and first normals.
Multiplying by any spectator uses the ordinary product rule and
preserves their equality. Differentiating in any free boundary
parameter does so as well. Thus the substitution is an identity
in every subsequent original contraction, not merely a comparison
at selected distinct roots. \(\square\)

In particular, for the original crossing at any fixed signed power,
\[
 \phi_N(R^nP_N^{\rm W}f)
 =(-1)^D C_{N,n}\sum_{j=0}^{D}
 \left.\frac d{dt}
 \left\{\sin t\,e^{inNt^2/(4\pi)}V_N(t)f(-2\cos t)\right\}
                                                    \right|_{\tau_j}.
                                                               \tag{8}
\]
Every derivative in this formula is retained.

## 3. Polynomial bounds up to the physical endpoints

**Theorem 2.** For every fixed \(H>0\), there is a constant \(C_H\)
such that
\[
 \sup_{\substack{|\Re t|\le\pi\\|\Im t|\le H}}|V_N(t)|
                                        \le C_H(1+\log N).
                                                               \tag{9}
\]
For every fixed derivative order \(r\),
\[
 \sup_{\substack{|\Re t|\le\pi\\|\Im t|\le H}}|V_N^{(r)}(t)|
                              \le C_{H,r}N^r(1+\log N). \tag{10}
\]
Thus no exponential factor in the level is introduced anywhere
on this physical rectangle, including its boundary layers.

**Proof.** It suffices first to bound (2). On the slightly enlarged
strip
\[
             -3/4\le\Re z\le N-1/4,\qquad
                         |\Im z|\le C_HN,
\]
write \(w_k=(z-k)/N\). The removable central pole and the two nearest
nonremovable cotangent poles give
\[
 |w\cot(\pi w)|\le C_H
       \left(1+\frac1{1-\Re w}+\frac1{1+\Re w}\right)
\]
when \(-1+1/(4N)\le\Re w\le1-1/(4N)\) and
\(|\Im w|\le C_H\). To verify the bound, use analyticity of
\(w\cot(\pi w)\) near zero and
\(|\sin\pi(x+iy)|^2=\sin^2\pi x+\sinh^2\pi y\)
near \(x=\pm1\); on the remaining compact set it is bounded.

As \(k\) varies, each reciprocal distance has the harmonic bound
\[
 \frac1N\sum_{k=0}^{D}\frac1{1\pm\Re w_k}
                                  \le C(1+\log N).
\]
Equation (2), written as
\((\pi/N)\sum_k w_k\cot(\pi w_k)\), is therefore
\(O_H(1+\log N)\), uniformly on this strip. This includes
\(g_N'(0)\).

For \(|\Re t|\le\pi\), one has
\(-1/2\le\Re\ell_N(t)\le N-1/2\), so (4) proves (9).
A \(t\)-disk of radius \(\theta/2=\pi/(2N)\) remains in the
slightly enlarged \(z\)-strip above; increase the height bound by
one, if needed. Cauchy's formula then proves (10).
\(\square\)

The polynomial representative itself and (4) need not be close
off the physical nodes. The bound is useful because their required
trace data are exactly equal before any contour is moved.

## 4. The central expansion and its nonzero logarithmic coefficient

Let \(a<\pi\) and \(H<\infty\) be fixed. On
\(|\Re t|\le a,\ |\Im t|\le H\), choose the branch of
\(\log\cos(t/2)\) that is real at real \(|t|<\pi\).
Then
\[
 \boxed{\displaystyle
 V_N(t)=\sigma\left[
 2\log N+
 2\{1+\gamma-\log\pi+\log\cos(t/2)\}\right]
                    +O_{a,H}\left(\frac{\log N}{N^2}\right).}
                                                               \tag{11}
\]
Here \(\gamma\) is Euler's constant. The expansion is holomorphic
and holds with every fixed derivative on smaller strips. In
particular \(V_N(t)/(2\sigma\log N)\to1\) there, and \(V_N\)
has no zero on any such fixed compact set for sufficiently large \(N\).

To prove the formula, set \(x=1/2-t/(2\pi)\), so
\(\ell_N(t)=Nx-1/2\). The canonical bulk expansion, with its
exact half offset, gives
\[
                     g_N'(Nx-1/2)
                      =\log(2\sin\pi x)+O_{a,H}(N^{-2}). \tag{12}
\]
Indeed the half-power correction in the logarithmic factorial
asymptotic vanishes at this offset. Differentiating its uniform
holomorphic remainder with respect to \(z\) introduces another
factor \(N^{-1}\). The real part of \(x\) stays in a fixed compact
subinterval of \((0,1)\), so its branches are regular.

At zero, differentiating the defining gamma product gives
\[
 g_N'(0)=\log(2\pi/N)-\gamma+
 \sum_{m\ge1}\{\psi(Nm+1)+\psi(Nm)-2\log(Nm)\},           \tag{13}
\]
where \(\psi=\Gamma'/\Gamma\). This remainder is \(O(N^{-2})\).
For a direct bound, at a positive integer \(k\) the bracket equals
\[
 -\int_0^\infty e^{-kt}
                   \left\{\coth(t/2)-2/t\right\}\,dt .
\]
The identity follows by summing the geometric series for harmonic
numbers and the integral for the logarithm. For \(x>0\),
\(0<\coth x-1/x<x/3\); the upper inequality follows by comparing
the nonnegative Taylor coefficients of
\((1+x^2/3)\sinh x-x\cosh x\).
Thus the bracket has modulus at most \(1/(6k^2)\), and the sum
in (13) has modulus at most \(\pi^2/(36N^2)\).

Finally use \(2\cos\theta=2+O(N^{-2})\),
\(2\sin\theta/\theta=2+O(N^{-2})\), and
\(2\sin\pi x=2\cos(t/2)\). Equations (4),(12),(13)
give (11). For positive derivative orders the error can be
sharpened to \(O(N^{-2})\), since the \(\log N\) term is
constant in \(t\).

## 5. What happens when the original window is shifted

The meromorphic continuation must not be mistaken for an entire
periodic polynomial. Its poles are exactly
\[
 t_k=(D-2k)\theta,\qquad k\in\mathbb Z\setminus\{0,\ldots,D\},
\]
with residues
\[
                \operatorname*{Res}_{t=t_k}V_N(t)
                         =-4\sigma\sin\theta\,\lfloor k/N\rfloor .
                                                               \tag{14}
\]
Indeed the factorial recurrence implies
\(\operatorname{ord}_{z=k}G_N=\lfloor k/N\rfloor\) at integer
\(k\); its logarithmic derivative has that residue, and
\(d\ell_N/dt=-1/(2\theta)\). The first poles are at
\(t=\pm(\pi+\pi/N)\). They lie just beyond the original physical
window, not at its physical nodes.

The exact \(N\)-step factorial relation gives
\(g_N'(z+N)=g_N'(z)+\pi\cot(\pi z)\). Consequently
\[
 \boxed{\displaystyle
 V_N(t+2\pi)-V_N(t)
     =-2\sigma N\sin\theta\,\cot\bigl(\pi\ell_N(t)\bigr).}
                                                               \tag{15}
\]
For an integer number \(k\) of full periods, the right side is
multiplied by \(k\), because \(\cot(\pi(\ell_N-N))\)
is unchanged.

Thus polynomial bounds on one physical rectangle do not remove
the residues crossed by a real shift of the window. A microscopic
shift that reaches the first pole already needs its endpoint term.
A macroscopic number of such shifts must retain the corresponding
pole contributions and the exact defect (15). If the rest of an
integrand also has a pole there, its full Laurent product is required;
(14) alone is not a substitute for that residue calculation.

## 6. A source-level consequence for controlled trace contours

Consider an original trace or finite network of original traces for
which a complete contour proof is already available. Suppose its
contributing angle contours, including their endpoints, stay in fixed
rectangles \(|\Re t|\le\pi,\ |\Im t|\le H\); suppose the contributing
critical points stay in a fixed interior strip \(|\Re t|<\pi\).
Retain every complementary contour and every original index sector
in that proof.

Insert finitely many actual coupons \(P_N^{\rm W}=T\Pi_0\) at specified
trace vertices, with arbitrary original spectator factors left in
place. Replace them by (4) before using the contour identity. This
is exact by Theorem 1, also for repeated coupons at the same vertex.
Theorem 2 preserves every strict exponential gap in the original
proof. It costs only a fixed power of \(N\) and \(\log N\), including
when derivatives occur on an endpoint current.

Near a contributing critical point the factor (11) has a nonzero
leading coefficient. For one such coupon the original Gaussian
amplitude is multiplied by \(V_N(t_*)\), with the same relative
\(O(N^{-1})\) expansion when the original local proof had that error.
Its derivative ratios are bounded on the fixed saddle chart, so the
usual parameter-uniform Gaussian estimate applies to this
\(N\)-dependent amplitude. With \(r\) coupons the leading factor
is
\[
                         (2(-1)^N\log N)^r(1+O(1/\log N)).
                                                               \tag{16}
\]
The original geometric exponential action is unchanged.

This is a preservation statement for a complete contour proof,
not a construction of a missing cycle. A contour crossing the poles
in (14), or a change of logarithmic window, must first incorporate
the resulting endpoint currents. Multiple competing critical
contributions also retain their original relative phases; a
previously unknown cancellation between them is not resolved by
(16).

For a concrete actual application, take the terminal source with
\(|p|\ge64\) and insert the coupon at its filled vertex:
\[
 H^{\rm W}_{p,N}(u)
       =\phi_N^{(t)}\bigl(R^pP_N^{\rm W}K_N(t,u)\bigr).
\]
Its complete contour proof uses the fixed central rectangle of the
large-power theorem. Omitted wires and real outer angles remain
controlled by the polynomial full Hermite norm of the coupon.
Theorems 1--2 handle its full central current. Therefore, on the
same sufficiently small boundary disk,
\[
 H^{\rm W}_{p,N}(u)
 =\epsilon_{p,N}A_p(u)V_N(t_p(u))
                    e^{NW_p(u)}(1+O_p(N^{-1})).          \tag{17}
\]
Its whole-boundary exponential bound is the original one, with
a larger polynomial prefactor. Formula (11) proves that the displayed
geometric contribution is nonzero. This is a coherent source
asymptotic, not just an operator-norm upper bound.

The same replacement is available at any finitely many traced vertices
of the proved recursive high-valence construction: all its original
trace rectangles satisfy these hypotheses. The leading action and
volume remain the same; the specified Ward coupons contribute the
known logarithmic factors. This does not extend that volume theorem
to arbitrary low-valence regions, whose complete contours have yet
to be established.

## 7. An actual odd Ward current can have the geometric rate

This consequence rules out treating the odd current as an exponentially
small error merely because its full Hermite norm is polynomial.

Let \(w\) be a fixed odd Ward power, let
\(\rho_N=2i\sin(\pi/N)\), and
\(\kappa_N=\exp(\pi iD^2/(2N))\). The exact turned current from
the signed Ward theorem is
\[
 \mathcal C_{w,N}
 =T(R^{-1}W_w)
 =\kappa_N^{-1}\left[
       2P_N^{\rm W}+(N-1-w)(-1)^N\rho_N I\right].       \tag{18}
\]
Here \(W_w\) denotes that theorem's exact spectral-shift Ward
difference, not a stationary action. Its original fixed logarithm
convention is retained in \(\kappa_N\).

Contract this actual current against a controlled terminal exterior:
\[
 \mathcal J_{w,p,N}(u)
       =\phi_N^{(t)}\left[R^pK_N(t,u)\mathcal C_{w,N}\right],
                           \qquad |p|\ge64.
\]
Equations (17)--(18), with the undeformed terminal asymptotic, give
\[
 \mathcal J_{w,p,N}(u)
 =\kappa_N^{-1}\epsilon_{p,N}A_p(u)e^{NW_p(u)}
 \left[2V_N(t_p(u))
       +(N-1-w)(-1)^N\rho_N+O_p(\log N/N)\right].        \tag{19}
\]
In particular, uniformly on a smaller complex boundary disk,
\[
 \boxed{\displaystyle
 \frac{\mathcal J_{w,p,N}(u)}
       {4(-1)^N\kappa_N^{-1}\log N\,H_{p,N}(u)}
                                      \longrightarrow1.}       \tag{20}
\]
The quotient is defined for all sufficiently large levels by the
nonzero terminal packet. Thus this genuine Ward contribution has
the same geometric exponential rate as its exterior, with a
nonzero logarithmic leading factor.

For a fixed nonzero even \(w\), the exact turned current is already
the scalar \(wN(-1)^N\rho_N\kappa_N^{-1}I\); its contraction
also has the same exterior rate. The zero Ward power gives zero.
These facts do not identify the rate of a general sum of currents
or exclude cancellations between its terms. They show precisely why
a full-source contour proof must assemble the currents with their
phases, even after polynomial norm bounds have been proved.

## 8. Reproduction

Run
~~~sh
python3 experiments/check_odd_ward_logarithmic_factorial.py \
  --precision 100 \
  --output repro/results/research-odd-ward-logarithmic-factorial.json
~~~

The script
[check_odd_ward_logarithmic_factorial.py](../experiments/check_odd_ward_logarithmic_factorial.py)
constructs the original Newton polynomial from its exact coefficients,
then compares its values and angular derivatives with (4), evaluated
from the independent finite cotangent formula. The
[saved results](../repro/results/research-odd-ward-logarithmic-factorial.json)
contain all 299 physical nodes at levels \(N=2,\ldots,24\).
The largest relative discrepancy is below \(1.07\cdot10^{-97}\)
at 100 decimal digits. Twelve off-grid period-defect checks also
passed, with largest relative discrepancy below \(1.30\cdot10^{-100}\).

The record includes twelve finite comparisons with the expansion
(11), at \(N=32,64,128,256\) and three fixed complex angles.
These are normalization diagnostics. The all-level identities,
rectangle estimates and source conclusions are established by the
written proofs, not inferred from those samples.



