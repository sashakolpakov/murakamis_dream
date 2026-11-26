# The complete conditional packet for all real neighbors

Research proof, 4 November 2026. This extends the lower-height contour
argument to every compact real subset of \((0,1/2)^2\), for both
conditional types. It is a theorem for the original single conditional
source, not for the remaining coherent outer sum.

## 1. The upper interpolation with its original period multiplier

Use the same marked interpolation \(P_N\) and lower-half functions
\(g_-,a_-\) as in
[the lower-half factorial theorem](research_lower_half_factorial_continuation.md).
Schwarz reflection of its sine Gamma product gives the exact complex
identity
\[
 P_N(w)=
 e^{-i\pi w(w+1)/N+i\pi w}\,
              \overline{P_N(\overline w)}.                   \tag{1}
\]
Define on the entire upper half-plane
\[
 \begin{split}
 g_+(z)&=\overline{g_-(\overline z)}+i\pi(z-z^2),\\
 a_+(z)&=e^{-i\pi z}\overline{a_-(\overline z)}.
 \end{split}                                                   \tag{2}
\]
These are holomorphic, and \(a_+\) is nonzero. The lower-half
asymptotic and (1) give, uniformly on every compact upper-half set,
\[
 P_N(Nz)=\sqrt N\,a_+(z)e^{Ng_+(z)}
 \exp\left\{\frac{\pi\cot\pi z}{12N}+O(N^{-3})\right\}.    \tag{3}
\]
The same statement holds with fixed derivatives on smaller compact
sets. This is an exact reflection of an already uniform expansion,
not continuation of its error bound across a factorial wall.

On the original strip, \(g_+\) is the original normalized marked
primitive and \(a_+(z)=e^{-i\pi z/2}\sqrt{2\sin\pi z}\).
Their branches agree there by the exact Schwarz identity, or by their
continuous positive-real sine values followed by holomorphy. Globally,
\[
 g_+(z+1)=g_+(z)-2\pi iz,\qquad a_+(z+1)=-a_+(z).           \tag{4}
\]
Thus (3) retains the full-period multiplier
\(P_N(N(z+1))=(1-e^{-2\pi iNz})P_N(Nz)\): in the upper
half-plane its dominant factor is \(-e^{-2\pi iNz}\).
The upper leading phase is not replaced by a periodic disk primitive.

## 2. The whole upper horizontal maximum

For real \(0<a,b<1/2\), let \(Q_{\epsilon,-}\) use \(g_-\)
and \(Q_{\epsilon,+}\) use \(g_+\), with the same original chirp
\(2\pi ias\). The two definitions agree with the original phase
on their respective portions of the regular strip. Equation (2) gives
\[
 \begin{split}
 Q_{\epsilon,+}(s;a,b)
 &=\overline{Q_{\epsilon,-}(\overline s;a,b)}\\
 &\quad+i\pi\{a(1-a)+b(1-b)+2s(a-b)+\epsilon(s^2-s)\}.
 \end{split}                                                   \tag{5}
\]
For \(y>0\), set \(R=e^{-2\pi y}\), and use the lower circular
functions \(J_R,D_{c,R},H_{\epsilon,R}\) from
[the full-period reflection theorem](research_mixed_negative_height_full_period.md).
Then
\[
 U_y(x):=\Re Q_{\epsilon,+}(x+iy)
 =H_{\epsilon,R}(x)
                 -2\pi y\{a-b+\epsilon(x-1/2)\}.             \tag{6}
\]
For \(0<x<1/2\), that theorem's strict second-difference inequality
therefore gives
\[
 U_y(x)-U_y(1-x)
 =D_{a,R}(x)+D_{b,R}(x)-2\epsilon J_R(x)
                         +2\pi\epsilon y(1-2x)>0.           \tag{7}
\]
At the two full-period endpoints,
\[
                         U_y(1)=U_y(0)-2\pi\epsilon y.       \tag{8}
\]

**Lemma 1.** If the selected original root has positive height
\(h_*>0\), its real coordinate is the unique nondegenerate global
maximum of \(\Re Q_{\epsilon,+}(x+ih_*)\) on \([0,1]\).
The whole high half has a strict gap. These gaps are uniform on
compact real parameter sets, including limits with \(h_*\downarrow0\).

Indeed the
[real-contour theorem](research_mixed_real_conditional_contour_geometry.md)
already proves the unique maximum on \([0,1/2]\) for both types,
including positive selected heights. Its exact type-four height bound
is essential in that proof. Equation (7) compares every interior
high-half point with its low-half mirror; (8) handles the last
endpoint, and the strict low-half endpoint inequalities handle the
others. At height zero the same comparison is the continuous lower
boundary inequality already proved in the reflection theorem.

## 3. Exact end joins and both alias directions

Write \(T_N\) for the original interpolated row (1) of
[the lower conditional packet](research_mixed_global_lower_conditional_packet.md).
Its midpoint real sides remain
\(l_N=-1/(2N)\), \(r_N=1-1/(2N)\). The exact finite reflection
at the left midpoint has no order-one height correction:
\[
 |T_N(l_N+iy)|=|T_N(l_N-iy)|
           e^{-2\pi Ny\{a-b-\epsilon/2\}}\qquad(y\ge0).
                                                                    \tag{9}
\]
The lower midpoint estimate and (5)--(6) now imply, uniformly for
bounded \(y\ge0\),
\[
 |T_N(l_N+iy)|\le C_KN^{-\epsilon/2}
                    e^{N\Re Q_\epsilon(iy+0^+)}.            \tag{10}
\]
This is the original right-boundary lift at \(\Re s=0\).
The exact real-neighbor inequality
\(|T_N(r_N+iy)|\le |T_N(l_N+iy)|\) holds for both signs of
\(y\), so it controls the right midpoint as well.

The real-contour theorem proves that the boundary phase is strictly
increasing away from zero in either vertical direction. Therefore
the positive selected end joins from zero to \(h_*\) have their
maximum at \(h_*\), strictly below the saddle. Extending them to
\(h_*+\tau\) preserves a uniform gap for a sufficiently small fixed
\(\tau>0\), on compact parameter sets.

The literal row reflection on all real \(x\) is
\[
 \frac{|T_N(x-iy)|}{|T_N(x+iy)|}
 =e^{2\pi Ny\{a-b+\epsilon(x-1/2)\}+\epsilon\pi y}.          \tag{11}
\]
On a compact real outer set and \(x\in[0,1]\), the absolute value
in braces is at most \(\Lambda_K<1\). Hence an upper selected-side
bound transfers to the lower cotangent remainder, and a lower
selected-side bound transfers to the upper one, with the same
exponential reserve
\(2\pi N(1-\Lambda_K)y\). The factors \(e^{\pm\epsilon\pi y}\)
are bounded at the bounded contour heights. The midpoint extension
by \(O(N^{-1})\) costs only another bounded factor. Thus neither
alias is omitted when the selected side changes sign.

## 4. All real neighbors

**Theorem 2.** Let \(K\Subset(0,1/2)^2\) be arbitrary, and let
\(\mathcal L_{\epsilon,N}\) be the fixed canonical finite sum in
(1) of the lower conditional packet. For both \(\epsilon=0,1\),
uniformly on \(K\),
\[
 \mathcal L_{\epsilon,N}(a,b)=
 N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}\,A_\epsilon(s_*;a,b)}
      {\sqrt{-Q_{\epsilon,ss}(s_*;a,b)}}
 e^{NQ_\epsilon(s_*;a,b)}\{1+O_K(N^{-1})\}.                 \tag{12}
\]
Here \(s_*\) is the global original zero-lift root, \(Q_\epsilon\)
at that root is its original regular-strip phase, and
\[
 A_\epsilon(s;a,b)=e^{i\pi(\epsilon s-a-b)/2}
 \frac{\sqrt{2\sin\pi(s+a)}\sqrt{2\sin\pi(s+b)}}
      {\{\sqrt{2\sin\pi s}\}^{2+\epsilon}}.                \tag{13}
\]
Every root and square-root branch is the same as in the earlier
conditional source. The coefficient is nonzero, so the full canonical
sum is nonzero for all sufficiently large levels, uniformly on \(K\).
In particular this holds for every original physical conditional
in the compact real square, along both level parities.

For a proof split \(K\) into its closed nonpositive- and nonnegative-
selected-height parts. The lower packet already handles the former.
On the latter use the same full midpoint residue rectangle and the
exact \(+N\) zero mode. Choose \(Y=h_*+\tau\). Lemma 1 and a
uniform analytic Taylor estimate at the nondegenerate root give
\[
             \max_{0\le x\le1}\Re Q_{\epsilon,+}(x+iY)
                              \le M+C_K\tau^2.              \tag{14}
\]
The compact gap away from the root and the full reflection inequality
give this estimate uniformly as \(h_*\downarrow0\). Equation (3)
bounds the entire upper horizontal finite interpolation, including
all shifted walls. Equation (11) then bounds the other horizontal
alias. The penalty \(2\pi N(1-\Lambda_K)Y\), with \(Y\ge\tau\),
strictly exceeds the quadratic cost when \(\tau\) is sufficiently
small. Equations (9)--(10), boundary monotonicity and the exact
midpoint cotangent bound control every vertical remainder.

Deform the zero mode through the actual root at height \(h_*\) on
a fixed small symmetric central interval. Put its exterior intervals
at \(h_*+\tau\), retaining the short central vertical joins and
the two end joins. All exterior intervals stay above \(\tau\), so
(3) is uniform even when a selected height is zero. Their strict
phase gap, and those of the joining segments, follow exactly as in
the lower proof using Lemma 1. Only the central regular-strip
segment is used for the Gaussian calculation. Its coefficient and
power are consequently the unchanged (12)--(13).

At height zero either the upper or lower indentation is valid; their
central original phase and amplitude agree. Compactness on each of
the two closed parts gives uniform constants, whose larger values
work on \(K\). This is not a pointwise argument with constants
diverging when the critical height changes sign.

## 5. Exact type-three symmetry and scope

As an independent normalization check, at \(\epsilon=0\) one has
\[
 T_{0,N}(s;a,b)=\Omega_N(a,b)\,
             \overline{T_{0,N}(\overline s;b,a)},\quad
 \Omega_N=e^{i\pi N\{a(1-a)+b(1-b)\}-i\pi(a+b)}.            \tag{15}
\]
The factor has unit modulus for real neighbors, and summing gives
the identical relation for the two full canonical finite sums.
The quadratic cotangent equation gives
\(\Im S=(P-Q)/(2\Re S+P+Q)\); hence \(h_*\le0\) exactly
when \(a\le b\). Thus (15) also extends type three directly
from the lower theorem. The proof above additionally handles
type four, for which the corresponding Schwarz identity has an
index-dependent chirp and is not a constant symmetry.

Theorem 2 is uniform for real neighbors. A fixed complex-neighborhood
source statement would additionally require preservation of the exact
midpoint and alias bounds under complex parameter perturbations.
No such statement, no full taper-domain dominance, and no lower
bound after the remaining outer sum is inferred here.

Reproduction:

    python3 experiments/check_mixed_all_real_conditional_packet.py

The [focused exact checker](../experiments/check_mixed_all_real_conditional_packet.py)
retains all input proof, script and record bindings. It verifies fifteen
upper phase, symbol, reflection, carrier and normalization identities,
and ninety exact type-three finite symmetry comparisons at levels
2, 3, 4, 5 and 6. The contour inequalities are the analytic arguments
above, not numerical level extrapolations.
