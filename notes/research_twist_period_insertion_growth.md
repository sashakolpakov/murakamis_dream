# The nilpotent term in a twist-period shift has augmented growth

The exact period law for the original crossing contains a nilpotent term. That term is not generally a polynomial-size remainder. For a vertex of any fixed positive degree and any fixed signed crossing power, its insertion has a nonzero asymptotic at the complete augmented rate. The uninserted source has a strict loss below that rate, even when its smaller geometric asymptotic is not yet known.

Consequently a level-dependent replacement \(n\mapsto n+2Nk\) does not approximate the fixed short-power source. It introduces a larger contribution, which cancels exactly when the short source is recovered by finite differences.

## 1. The original source and the period identity

Fix \(d\ge1\), \(n\in\mathbb Z\), and use the full original algebra and trace. Put \(D=N-1\), \(\eta=(-1)^D\),
\[
 C_{N,n}=\exp\frac{\pi i nD^2}{4N},\qquad
 U_N=\eta R^{2N}-1,\qquad U_N^2=0.
\]
For the complete original edge kernel
\[
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u)
\]
define the boundary polynomials
\[
 P_{d,n,N}(\mathbf u)
 =\phi_N\left(R^n\prod_{j=1}^dK_N(t,u_j)\right),\qquad
 B_{d,n,N}(\mathbf u)
 =\phi_N\left(R^nU_N\prod_{j=1}^dK_N(t,u_j)\right).             \tag{1}
\]
Both retain every wire index and the original first normal derivatives. The exact period law gives, for every integer \(k\),
\[
 P_{d,n+2Nk,N}=\eta^k(P_{d,n,N}+kB_{d,n,N}).        \tag{2}
\]
All framing factors outside this original source remain separate. No ordinary-color interpretation of \(B\) is assumed.

Write
\[
 M_\infty=\psi(0,0)=4G/\pi,\qquad
 G=\sum_{m\ge0}\frac{(-1)^m}{(2m+1)^2},
\]
where the edge phase and amplitude obey
\[
 K_N(t,u)=N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \quad a_e(0,0)=1/4,
\]
on a sufficiently small complex chart about zero. To use this as an expansion of the full kernel, first compare its action with the original omitted-wire rate: \(\Re\psi(0,0)=M_\infty\), whereas the omitted indices lose \(\pi/100\). Continuity permits shrinking the chart so that the omitted terms remain exponentially smaller than its selected action. For a fixed product of \(d\) kernels, shrink the common chart again so that the sum of its selected actions remains strictly above the rate of every assignment with an omitted wire. The proof below performs that comparison before discarding anything. In particular
\[
 \psi_t(0,u)=0,\qquad \psi_{tt}(0,u)=-\cos(u/2)/(2\pi).
                                                               \tag{3}
\]

## 2. An exact formula for the insertion

The original spectral angles are
\[
 \tau_j=\frac{\pi(D-2j)}N,\qquad 0\le j<N.
\]
At these angles the crossing value and first normal are represented by
\[
 R^n(\tau_j)=C_{N,n}e^{inN\tau_j^2/(4\pi)},\qquad
 \partial_tU_N(\tau_j)=iN^2\tau_j/\pi,\qquad U_N(\tau_j)=0.
\]
Indeed \(R_t'/R=iNt/(2\pi)\) at the physical nodes; differentiating \(\eta R^{2N}-1\) gives the stated normal. The original derivative-sampling trace is
\[
 \phi_N(F)=\eta\sum_{j=0}^{D}
           \left.\frac{d}{dt}\{\sin t\,F(-2\cos t)\}\right|_{\tau_j}.
\]
Therefore, for any original polynomial \(f\),
\[
 \boxed{
 \phi_N(R^nU_Nf)
 =\frac{i\eta C_{N,n}N^2}{\pi}
   \sum_{j=0}^{D}\tau_j\sin\tau_j\,
       e^{inN\tau_j^2/(4\pi)}f(-2\cos\tau_j).}       \tag{4}
\]
The derivative of \(f\) disappears because the value of \(U_N\) is zero. Its first normal does not disappear.

Equivalently, at the distinct double roots \(c_j=2\cos\theta_j\), \(\theta_j=(2j+1)\pi/N<\pi\),
\[
 \phi_N(R^nU_Nf)
 =2i\eta N\sum_j(D-2j)\sin\theta_j\,
                         R(c_j)^n f(c_j).          \tag{5}
\]
Thus the insertion is a weighted value trace. Those values need not have polynomial growth: the actual edge kernels in (1) furnish the exponential example below.

As a normalization check independent of an edge kernel,
\[
 \phi_N(U_N)=\frac{i\eta N^2}{\sin(\pi/N)}.          \tag{6}
\]
To prove this, pair the two equal spectral roots and use
\[
 \sum_{j=0}^{N-1}(D-2j)\sin\frac{(2j+1)\pi}{N}
       =\frac{N}{\sin(\pi/N)}.
\]
The latter follows by differentiating the finite geometric sum. Since \(\phi_N(1)=0\), the closed original trace already gives
\(\phi_N(R^{2Nk})=i\eta^{k+1}kN^2/\sin(\pi/N)\).

## 3. Nonzero asymptotics for every fixed degree and power

Put
\[
 W_0(\mathbf u)=\sum_{j=1}^d\psi(0,u_j),\qquad
 A_{d,n}(\mathbf u)=\sum_{j=1}^d\cos(u_j/2)-in.
\]

**Theorem.** For every fixed \(d\ge1\) and \(n\in\mathbb Z\), on a sufficiently small fixed complex polydisk about \(\mathbf u=0\),
\[
 \boxed{
 B_{d,n,N}(\mathbf u)=
 2i\eta C_{N,n}\,
 \frac{\prod_{j=1}^d a_e(0,u_j)}{A_{d,n}(\mathbf u)^{3/2}}\,
 N^{-3(d-1)/2}e^{NW_0(\mathbf u)}(1+O_{d,n}(N^{-1})).}          \tag{7}
\]
The power uses the branch with positive real part for \(A_{d,n}^{1/2}\). The amplitude is holomorphic and nonzero. All fixed parameter derivatives have the same error order on smaller polydisks. In particular,
\[
 B_{d,n,N}(0)\sim
 \frac{2i\eta C_{N,n}4^{-d}}{(d-in)^{3/2}}\,
 N^{-3(d-1)/2}e^{NdM_\infty}.                     \tag{8}
\]

**Proof.** Retain \(I=[1/5,3/10]\) in each edge kernel. The complete Hermite bounds in [the original finite estimates](../papers/circle-tree-volume/finite-bounds.tex) show that an omitted wire loses at least \(\pi/100\) below \(dM_\infty\). Multiplication by \(R^nU_N\) and closing have polynomial cost: \(n\) is fixed, and the values of \(U_N\) vanish while its first normals are \(O(N^3)\). This proves the same strict tail bound for (1), with every original index included.

For the retained kernels, the full real-period angular bound in [the edge proof](../papers/circle-tree-volume/edge-packet.tex) is strictly smaller away from \(t=0\). For example, outside any fixed small interval it bounds the product by a polynomial times \(e^{N(dM_\infty-c)}\). Formula (4) adds only polynomial factors and a unit chirp at real \(t\). Both statements extend to a sufficiently small complex boundary polydisk, by the uniform angular estimates or the polynomial degree bound. Shrink the polydisk so the losses also remain strict relative to \(\Re W_0(\mathbf u)\).

In the remaining interval, insert the full local edge expansion into (4). Separate evenness gives a critical point at \(t=0\) for every \(\mathbf u\), with phase
\[
 \sum_j\psi(t,u_j)+\frac{in}{4\pi}t^2
 =W_0(\mathbf u)-\frac{A_{d,n}(\mathbf u)}{4\pi}t^2+O(t^4).
\]
Its real quadratic part is strictly negative after shrinking the polydisk. The prefactor \(\tau\sin\tau\) has a double zero, with leading term \(\tau^2\).

The physical nodes have spacing \(2\pi/N\); the two parities differ only by a half-step. Replacing their local sum by \(N/(2\pi)\) times the corresponding integral has relative error \(O(N^{-1})\). One direct justification is the shifted trapezoid remainder bounded by a constant times \(h^2\int|f''|\), \(h=2\pi/N\), after a smooth fixed cutoff. For \(f=t^2e^{-cNt^2}\), this error is \(O(N^{-5/2})\), compared with an integral of order \(N^{-3/2}\). The same bounds hold for the analytic amplitude and complex Gaussian with uniformly positive real quadratic coefficient. The cutoff errors have a strict exponential loss.

The required moment is
\[
 \int_{\mathbb R}t^2
       e^{-NA_{d,n}t^2/(4\pi)}\,dt
       =4\pi^2N^{-3/2}A_{d,n}^{-3/2}.
\]
Multiplying by the node density \(N/(2\pi)\), the trace factor
\(i\eta C_{N,n}N^2/\pi\), and the edge factors
\(N^{-3d/2}\prod a_e(0,u_j)\) gives (7). Taylor expansion provides the relative error; Cauchy's formula gives parameter derivatives. The same argument yields any fixed inverse-power order, though only the first is asserted here. \(\square\)

## 4. The uninserted source has a strict augmented-rate loss

A smaller geometric asymptotic for \(P\) is not required for the following fact.

**Proposition.** For every fixed \(d\ge1,n\in\mathbb Z\), there are constants \(c_{d,n}>0,C,p\) and a small complex boundary polydisk such that
\[
 |P_{d,n,N}(\mathbf u)|
 \le CN^p e^{N(\Re W_0(\mathbf u)-c_{d,n})}.         \tag{9}
\]

**Proof.** First discard the original wire tails and the real angles outside \(a_0=6/25\), exactly as above, retaining their strict losses. The exact midpoint trace identity in [the internal-vertex proof](research_high_degree_short_internal_vertex.md), Section 5, applies independently of its later degree/power condition:
\[
\begin{split}
 {\cal D}^{a_N}_{n,N}f_N
={}&-\frac{N^2C_{N,n}}{\pi i}
 \int_{-a_N-ih}^{a_N-ih}
 g_N(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt\\
 &+\frac{\eta N^2C_{N,n}}{\pi}
 \int_{-h}^{h}\frac{g_N(a_N+iv)}{4\cosh^2(Nv/2)}\,dv,
\end{split}                                                    \tag{10}
\]
where \(f_N=\prod_jK_{N,I}(t,u_j)\),
\(g_N=\sin t\,f_Ne^{inNt^2/(4\pi)}\), and \(a_N=a_0+O(1/N)\) is an actual midpoint. No term of this identity is dropped.

At zero boundary angle, \(\psi_{tt}(t,0)=-\sec(t/2)/(2\pi)\). On the relevant small rectangle its modulus is less than \(1/6\), while on the real interval
\(\psi(t,0)\le M_\infty-t^2/(4\pi)\).
For \(h\le1/100\), the lower horizontal exponent is therefore at most
\[
 dM_\infty-\frac d{4\pi}t^2+\frac{|n|}{2\pi}|t|h
                     +\frac d{12}h^2-h
 \le dM_\infty-h+
     \left(\frac d{12}+\frac{n^2}{4\pi d}\right)h^2.             \tag{11}
\]
The term \(-h\) is from the exact first charge. The full rational denominator in (10) is uniformly bounded at this fixed height.

Put \(C_0=d/12+n^2/(4\pi d)\) and
\(\Delta_0=da_0^2/(4\pi)\). Choose
\[
 0<h\le\min\left\{\frac1{100},
       \frac1{4(C_0+1)},\frac{\Delta_0}{4(d+|n|+1)}\right\}.     \tag{12}
\]
Then (11) loses at least \(3h/4\). The vertical endpoint has phase at most
\[
 dM_\infty-\Delta_0+
             \frac d{12}v^2+\frac{|n|a_N}{2\pi}|v|
 \le dM_\infty-3\Delta_0/4+o(1);
\]
here even the additional loss from \(\cosh^{-2}(Nv/2)\) can be ignored. The actual \(\sin t\) factors and lengths cost only polynomial factors. All the original tails and both contours therefore have a strict loss. The estimates persist near \(\mathbf u=0\), relative to \(\Re W_0\), after shrinking the polydisk. This proves (9). \(\square\)

This argument establishes a loss below the augmented rate. It does not identify the smaller rate of \(P\).

## 5. What the period law does and does not transfer

Let \(k_N\ne0\) be integers with \(\log(1+|k_N|)=o(N)\). Equations (2), (7), and (9) imply
\[
 P_{d,n+2Nk_N,N}(\mathbf u)
 =\eta^{k_N}k_N B_{d,n,N}(\mathbf u)
       (1+O(N^p e^{-cN})).                         \tag{13}
\]
Thus the level-dependent long powers have augmented rate
\(dM_\infty\) at complete boundary angle, for every fixed \(d,n\).
Their dominant term is the nilpotent insertion, not the fixed short source.

Conversely the exact reconstruction is
\[
 P_{d,n,N}
 =2\eta^{-k}P_{d,n+2Nk,N}
       -\eta^{-2k}P_{d,n+4Nk,N},\qquad k\ne0.       \tag{14}
\]
The whole \(B\) term cancels exactly. Since \(B\) has a complete local inverse-power expansion and \(P\) has the strict loss (9), every algebraic order of that larger expansion cancels in (14). Recovering the smaller source therefore requires exponentially accurate information, not a finite number of long-power stationary-phase coefficients.

There is still a useful upper-bound transfer. For any norm on the boundary-polynomial space,
\[
 \|P_{d,n,N}\|
 \le3\max\{\|P_{d,n+2Nk,N}\|,\|P_{d,n+4Nk,N}\|\}.   \tag{15}
\]
There is no corresponding lower bound at the smaller fixed-source rate from the two long-power magnitudes alone. The explicit original sources (7)--(14) exhibit the obstruction, with the full boundary data retained.

For several period shifts the exact source is separately affine after its phases are removed. Applying the two-point identity in each coordinate gives a \(2^r\)-corner upper-bound transfer with factor \(3^r\). This finite-dimensional fact does not control the cancellation between its nilpotent-insertion coefficients. No multivertex asymptotic is asserted in this note.

## 6. Reproduction

The standalone check compares (4) with the original triangular crossing matrix and the full Newton multiplication matrix, then compares its complete nodal sum with (8) at both parities:

~~~sh
python3 experiments/check_twist_period_insertion.py --output repro/results/research-twist-period-insertion.json
~~~

It retains every wire index and every physical node. The [saved values](../repro/results/research-twist-period-insertion.json) are normalization diagnostics, not inputs to the contour or Gaussian proofs.
