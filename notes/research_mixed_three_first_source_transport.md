# Finite source transport after a second type-three coordinate

Research deduction, 5 November 2026. The fixed original conditional
contour gives the finite upper bound needed after prefixes \((3,3)\)
and \((4,3)\), throughout the first collar and at the unchanged
third reference. The bound uses the original reference action plus
the exact allowance already paid by the pair comparison. It does
not assert a new nonzero packet at the moving target. No new root,
parameter cover, or source interpolation is introduced.

## 1. Actual path and the original finite source

Use the actual references and notation of
[the type-three phase deduction](research_mixed_three_first_vertical_phase.md).
The word has length at least three, its first two types are
\((3+\alpha,3)\), and its third type is \(3+\epsilon\).
Write \(r_2=b+ic\), keep \(B=r_3\) fixed and unselected, and put
\[
 A(k)=b+ik,\qquad k\in[\min(c,0),\max(c,0)],\qquad
 .267<b<.433,\quad -.065<c<.068.
 \tag{1}
\]
The actual ordinary/private union for \(B\) is
\[
 \begin{cases}
 .267<\Re B<.438,\quad -.065<\Im B<.068,&\epsilon=0,\\
 .24<\Re B<.363,\quad -.102<\Im B<-.001,&\epsilon=1.
 \end{cases}
 \tag{2}
\]
In particular all parameters and shifted central arguments below
remain in their original regular sine strips.

Let \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(X)=(rX;r)_j\). The literal conditional function is
\[
 C_{\epsilon,N}(X,Y)
   =\sum_{j=0}^{N-1}
       X^{-j}\frac{p_j(X)p_j(Y)}{P_j^{2+\epsilon}},
 \qquad X=e^{-2\pi iA},\quad Y=e^{-2\pi iB}.
 \tag{3}
\]
Every row is retained, including rows revived off the physical grid.
With the original primitive \(g\), its normalized central phase is
\[
 q_\epsilon(w;A,B)
 =g(w+A)+g(w+B)-(2+\epsilon)g(w)+2\pi iAw-g(A)-g(B).
 \tag{4}
\]
At \(A=r_2\), let \(s_*\) be the original conditional root and
set \(m_*=\Re q_\epsilon(s_*;r_2,B)\).

The [reduced-disk conditional theorem](research_mixed_reduced_disk_conditional_packets.md)
applies at this reference when the third block is ordinary. When
the length is three, use instead the
[terminal conditional theorem](research_mixed_terminal_conditional_packet.md).
Both are the same finite function (3). Their contour proofs retain
the fixed real cuts \(\ell=.15,u=.49\), both horizontal aliases
at heights \(\pm.2\), all half-grid vertical currents, and the
zero mode moved to the original height \(\Im s_*\). All these
central paths lie in
\[
                    K=[.15,.49]+i[-.2,.2].
 \tag{5}
\]
At the reference the absolute real-tail sums and all noncentral
currents have a strict gap from \(m_*\); the central zero mode
has upper rate \(m_*\). These absolute contour bounds, not merely
the value of the completed sum, are the input used below.

## 2. Every fixed central phase has the same angular allowance

Write \(P=\cot\pi A(k)=p+i\beta\) and
\(C=\cot\pi w=u_0+iv_0\). The actual path bounds already proved
in the phase deduction imply
\[
                  0<p<1,\qquad \beta>-.37.
 \tag{6}
\]
Indeed \(\Re\cot\pi(b+ik)\le\cot\pi b<1\), since
\(b>1/4\). For every \(w\in K\), one has \(u_0>0\).
The exact first marginal of (4) is
\[
 \partial_A q_\epsilon(w;A,B)
   =\log_{\rm R}(C+P)-\log_{\rm R}(C-i).
 \tag{7}
\]
This identity holds for a fixed index, not only at a conditional
root. It follows from
\((C+P)/(C-i)=e^{i\pi w}\sin\pi(w+A)/\sin\pi A\).
The two right-half-plane logarithms and the original regular-strip
logs agree at real parameters and continue throughout (1), (5).

The imaginary numerator of this ratio is
\[
                     u_0(1+\beta)+p(1-v_0).
 \tag{8}
\]
If \(v_0\le1\), it is positive immediately. Otherwise
\(\Im w<0\), \(\Re w<1/4\), and the cotangent formula gives
\[
 \frac{v_0-1}{u_0}
 =\frac{\cos(2\pi\Re w)-e^{-2\pi|\Im w|}}
        {\sin(2\pi\Re w)}
 \le\frac{\cos(.3\pi)-e^{-.4\pi}}{\sin(.3\pi)}
 <\frac7{16}<\frac{63}{100}.
 \tag{9}
\]
For fixed height, the fraction decreases with the real coordinate:
its derivative has the sign of
\(-1+e^{-2\pi|\Im w|}\cos(2\pi\Re w)<0\).
It increases with the height magnitude. The strict elementary
bounds used in (9) are
\(\cos(.3\pi)<3/5\), \(\sin(.3\pi)>4/5\), and
\(e^{-.4\pi}>1/4\). The first two follow from the exact
pentagon values; the last follows from
\(.4\pi<44/35<4/3<\log4\), using \(\pi<22/7\) and
\(\log2>2/3\). Thus (6), (9) also make (8) positive.

Both logarithms in (7) have arguments in \((-\pi/2,\pi/2)\).
It follows that, on the whole fixed index rectangle,
\[
 0<\Theta_w(k):=\Im\partial_Aq_\epsilon(w;A(k),B)<\pi,
 \qquad \partial_k\Re q_\epsilon=-\Theta_w(k).
 \tag{10}
\]
Define the same allowance as in the phase deduction,
\[
 a_c(k)=
 \begin{cases}0,&c\le0,\ c\le k\le0,\\
               \pi(c-k),&c\ge0,\ 0\le k\le c.
 \end{cases}
 \tag{11}
\]
Integrating (10) gives the pointwise bound
\[
 \Re q_\epsilon(w;A(k),B)
       \le\Re q_\epsilon(w;r_2,B)+a_c(k)
                             \qquad(w\in K).
 \tag{12}
\]
This includes the old central saddle-height segment, its joins,
and both alias contours. Their cotangent-kernel penalties do not
depend on \(A\) and remain unchanged.

## 3. Exact finite transport of every real tail row

For a row of (3) that is not identically zero because of its fixed
\(Y\) factor, differentiate its modulus off \(k=0\). Put
\[
 \mathcal P_t(x)=\frac{1-t^2}{1+t^2-2t\cos(2\pi x)}>0
                                      \qquad(0<t<1).
 \tag{13}
\]
The exact finite product, including its chirp, gives
\[
 \partial_k\log\left|
       X^{-j}\frac{p_j(X)p_j(Y)}{P_j^{2+\epsilon}}\right|
 =\begin{cases}
 -\pi j-\pi\displaystyle\sum_{h=1}^j
                   \mathcal P_{e^{2\pi k}}(b+h/N),&k<0,\\
 -\pi j+\pi\displaystyle\sum_{h=1}^j
                   \mathcal P_{e^{-2\pi k}}(b+h/N),&k>0.
 \end{cases}
 \tag{14}
\]
For negative \(k\) this is nonpositive; for positive \(k\)
it is at least \(-\pi j\). Integrating in the attenuation
direction and using \(j<N\) proves, for every original row,
\[
                  |\mathrm{row}_j(A(k),B)|
        \le e^{Na_c(k)}|\mathrm{row}_j(r_2,B)|.
 \tag{15}
\]
The zero row and fixed \(Y\)-zeros satisfy this directly.
Continuity gives (15) at \(k=0\), also when the moving product
acquires a physical zero there. No division by that zero or
Riemann-sum approximation is used. In particular the absolute
left and revived right tails of the original finite sum transport
with exactly the same allowance (11).

## 4. Keeping the original contour gives the finite upper bound

**Theorem 1.** Uniformly on the actual path (1)--(2), for every
fixed \(\eta>0\) and both level parities,
\[
 \begin{split}
 |C_{\epsilon,N}(e^{-2\pi iA(k)},e^{-2\pi iB})|
            |d_N(e^{-2\pi iB})|^{\epsilon/2}
 \le C_\eta N^A\exp N\{
       \Re\phi_{0\epsilon}(r_2,B)+a_c(k)+\eta\}.
 \end{split}
 \tag{16}
\]
The third reference is unselected. Its halfweight in (16) is the
same fixed factor throughout the transport.

*Proof.* Keep the exact contour decomposition already used at
\((r_2,B)\), including its half-grid cuts and its original central
height. The finite interpolation and all central arguments remain
regular for the new parameter \(A(k)\). Hence the same contour
identity holds; no root-dependent deformation is needed. Its
uniform regular-strip symbol has leading phase (4) and at most a
polynomial prefactor on this fixed compact set.

Equation (12) bounds every central contour integrand by its old
exponential upper rate plus \(a_c(k)\). The old weighted alias
and join bounds remain strict relative to \(m_*+a_c(k)\).
On the old central horizontal segment its reference upper rate
is at most \(m_*\), by the original saddle and real concavity.
Taking an absolute integral there is sufficient for an upper
bound; no new Gaussian or cancellation claim is required.
Equation (15) transports the two complete absolute real-tail sums.
Adding all these literal pieces proves the upper bound with rate
\(m_*+a_c(k)+\eta\).

For \(\epsilon=1\), the unchanged actual type-four argument
\(B\) has negative height bounded away from zero in (2).
The completed [Fourier-weight theorem](research_mixed_fourier_weight_continuation.md)
gives its unselected
halfweight rate \(-\Re g(B)/2\), with the actual forcing
retained. This is precisely the difference between the bare
conditional action \(m_*\) and
\(\Re\phi_{01}(r_2,B)\). For \(\epsilon=0\) there is
no such weight. Multiply by this fixed factor; none is divided
out. Combining its error with the contour errors into the one
arbitrary \(\eta\) proves (16). \(\square\)

The theorem uses the old critical point only to choose and bound
the original contour. It neither assumes nor needs that a moving
conditional root stays in (5). Its right side is the original
reference action plus (11), not the sharper moving phase from
equation (14) of the phase deduction.

## 5. The full first collar for the two second-three prefixes

**Corollary 2.** At the unchanged third reference, the literal
first-cap and first-two-edge product (15) of the phase deduction
has finite loss \(1/40\) for prefix \((3,3)\), and
\(1/50\) for prefix \((4,3)\), on the entire fixed first
collar \(0\le x_1\le\rho\). The first type-four selection,
when present, may be either allowed value. The second coordinate
is type three and the third remains unselected.

*Proof.* The original first-pair ceiling is
\(\mathcal C_\alpha(k)\) from (11) of the phase deduction.
Its equation (12) proves directly
\[
 \mathcal C_\alpha(k)+a_c(k)
  <M_{\alpha3}
          -\begin{cases}3/100,&\alpha=0,\\6/250,&\alpha=1.
            \end{cases}
 \tag{17}
\]
The same actual reference floors and collar choices used there
are retained. Add (16), and spend one total finite-source and
ordinary-color tolerance less than \(1/200\) or \(1/250\),
respectively. The reference rate is exactly
\(M_{\alpha3}+\Re\phi_{0\epsilon}(r_2,r_3)\).
The two second-coordinate tangent coefficients cancel by original
stationarity, as in equation (10) of that note. The third tangent
is not discarded: its target is unchanged here.

The full first \(d_N\), the entire first-cap private sum, both
conditional sums and the third coordinate's allocated halfweight
remain present. Both parities and each fixed ordinary color
derivative hold on the smaller color neighborhoods provided by
the original first-cap bounds. \(\square\)

This removes the small-reset requirement for this three-factor
comparison. It does not yet move the third target away from its
reference, attach an arbitrary boundary completion, or prove the
global open-source estimate. The physical seam still preserves
the neighboring height; it is the collar face that resets it.
