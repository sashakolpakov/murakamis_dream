# Angular tails on the shifted wire circle for every positive pair

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The original physical angles near \(\pi\) can be removed before
shifting the shared Fourier circle, uniformly for every fixed
positive internal pair \(n,p\ge3\). The proof has two ingredients:
a sharper complete-end kernel bound on the real tail, and a
uniform bound on the imaginary height of the actual shared wire.
The Fourier continuation is applied to each half-band source
separately; a product of two such sources is not reconstructed
from only \(N\) samples.

## 1. A real complete-end bound through the endpoint color

Put \(J_N=\lfloor(N-1)/2\rfloor\), \(c_0=2\cos(\pi/N)\), and
\(F_a(w)=K_N(c_a,w)\), with \(F_0=1\). The
[original physical-row recurrence](research_physical_row_riccati_transport.md)
has positive coefficients \(A_a>0\), \(q_a=C_a/A_a\ge0\).
In the variable \(\delta=c_0-w\), write \(P_a(\delta)=F_a(w)\).
Its difference form is
\[
 P_0=1,\qquad
 P_{a+1}-P_a=q_a(P_a-P_{a-1})+\frac{\delta}{A_a}P_a .
 \tag{1}
\]
At \(a=0\) the first term is zero.

**Lemma 1.** Every coefficient of \(P_a\) and of
\(P_{a+1}-P_a\) is nonnegative.

*Proof.* Start with \(P_0=1\) and
\(P_1-P_0=\delta/A_0\). Equation (1) preserves nonnegative
coefficients in both polynomials at every subsequent ordinary
row. It is used only through \(a=J_N-1\), where all its
coefficients are defined. \(\square\)

Fix \(0<T<\pi\), and write \(w_T=-2\cos T\). For all sufficiently
large levels,
\[
 |c_0-w|\le c_0-w_T\qquad(w_T\le w\le2).
 \tag{2}
\]
Indeed \(c_0>w_T\), and \(2-c_0<c_0-w_T\) eventually. Lemma 1
therefore gives
\[
 |F_a(w)|\le P_a(|c_0-w|)
       \le P_a(c_0-w_T)\le F_{J_N}(w_T).
 \tag{3}
\]
Let \(\mathcal L_N(w)\) be the original low-index complete-end
kernel. At odd levels it equals \(F_{J_N}(w)\). At even levels
the [exact Chebyshev interpolation](research_even_complete_low_kernel.md)
is a linear combination of the \(F_a(w)\) whose coefficient
absolute sum is \(O(\log N)\). Thus (3), followed by the
[absolute last-row normalization](research_last_physical_row_riccati.md)
at the single fixed color \(w_T<2\), proves
\[
 \sup_{w_T\le w\le2}|\mathcal L_N(w)|
       \le C N^A e^{N\Psi(T)},\qquad \Psi(T)=\psi(T,0).
 \tag{4}
\]
This argument does not extend a compact half-plane asymptotic
across its boundary. It uses the positive coefficients in the
exact finite recurrence.

The original radical has polynomial norm on the real interval.
Consequently (4) holds for the full complete-end kernel as well:
\[
 \sup_{T\le|t|\le\pi}|K_N(t,0)|
       \le C N^A e^{N\Psi(T)}.
 \tag{5}
\]
Every fixed ordinary normal has the same bound, with a larger
polynomial power, by Markov's inequality on the whole interval
\([w_T,2]\). In particular the endpoint color \(2\) is included.
The complete edge phase is positive for \(T<\pi\), decreases
there, and satisfies
\[
                         \Psi(T)\longrightarrow0\quad(T\to\pi).
 \tag{6}
\]
This also follows from its integral
\((2/\pi)\int_0^{\pi/2}\operatorname{arsinh}(\cos(T/2)\cot y)\,dy\)
by dominated convergence.

## 2. A uniform bound on the actual pair's wire height

Write the selected angles as \(t=a-iH\), \(r=b-iK\), and put
\[
 A=\cos^2(t/2),\qquad B=\cos^2(r/2),\qquad
 k=\frac{AB}{A+B}=\sin^2(\pi x_*),\qquad Y=\Im x_*>0.
 \tag{7}
\]
The [pair angle and height theorem](research_internal_pair_complete_edge_gap.md)
and the [wire-order theorem](research_positive_path_real_wire_order.md)
give
\[
 0<a,b<\pi/2,\quad 0<H,K<107/100,\quad |A|,|B|<1.
 \tag{8}
\]
In particular
\[
 \frac12<\Re A,\Re B<1,\qquad
                      0<\Im A,\Im B<\frac23 .
 \tag{9}
\]
For the last bound, use
\(\Im A=\sin a\,\sinh H/2\) and
\(\sinh(107/100)<4/3\). An elementary rational verification
of this scalar comparison is given below.

**Lemma 2.** At every actual positive internal pair,
\[
                              2\pi Y<\frac34 .
 \tag{10}
\]

*Proof.* First consider the whole rectangle
\(A=a_0+ib_0\), \(B=c_0+id_0\), with
\(1/2\le a_0,c_0\le1\) and \(0\le b_0,d_0\le2/3\).
For \(k=AB/(A+B)\),
\(\partial k/\partial A=B^2/(A+B)^2\).
Write
\[
 Q=c_0(a_0+c_0)+d_0(b_0+d_0),\qquad
 I=a_0d_0-b_0c_0 .
 \tag{11}
\]
These are the real and imaginary numerators of \(B/(A+B)\).
Both \(Q-I\) and \(Q+I\) are strictly positive.
For \(Q-I\), the only potentially negative term is
\(a_0(c_0-d_0)\); when \(d_0>c_0\), its resulting lower bound is
\(c_0^2+c_0+d_0^2-d_0\ge1/2\).
For \(Q+I\), when \(d_0<c_0\), a lower bound is
\(c_0^2-c_0/6+d_0^2+7d_0/6\ge1/6\).
The other cases have only nonnegative terms.
Thus \(Q>|I|\), and
\(\Re\{(B/(A+B))^2\}>0\).
It follows that \(\Im k\) increases with \(b_0\); by symmetry
it also increases with \(d_0\).

Raise both imaginary coordinates to \(2/3\). Direct division
now gives
\[
 \Im k\le\frac13\left(1+
       \frac{(a_0-c_0)^2}{(a_0+c_0)^2+16/9}\right)
       \le\frac{109}{300}<\frac38 .
 \tag{12}
\]
For the actual \(A,B\), the half-plane \(\Re A>1/2\) is
equivalent to \(|1/A-1|<1\). Convexity of this disk gives
\(|1/k-2|<2\), hence \(\Re k>1/4\).
The actual wire-order conclusion \(\Re x_*<1/4\) gives
\(\Re k<1/2\).

The elementary identity for \(k=\sin^2(\pi x_*)\) is
\[
                 \cosh(2\pi Y)=|k|+|1-k|.
 \tag{13}
\]
On \(1/4\le\Re k\le1/2\), \(0\le\Im k\le3/8\), its right
side is largest at \(\Re k=1/4,\Im k=3/8\). It is therefore
at most
\[
 \frac{\sqrt{13}+3\sqrt5}{8}
 <\frac{1033}{800}
 <1+\frac{(3/4)^2}{2}+\frac{(3/4)^4}{24}
 <\cosh(3/4).
 \tag{14}
\]
Strict increase of \(\cosh\) on positive reals proves (10).
\(\square\)

For completeness, \(\sqrt{13}<361/100\) and \(\sqrt5<56/25\)
prove the first rational comparison in (14). For \(x=107/100\),
successive terms of the tail of the hyperbolic-sine series,
starting at \(x^5/5!\), have ratio at most \(x^2/42\). Hence
\[
 \sinh x\le x+\frac{x^3}{6}
       +\frac{x^5}{120(1-x^2/42)}<\frac43 .
 \tag{15}
\]
All strict scalar comparisons here are rational after squaring
the two positive square-root bounds.

## 3. Transporting the whole omitted trace through the Fourier circle

Let \(\mathbf B_N(x)\) be the original full-jet interpolation,
with frequencies
\(\{-D/2,-D/2+1,\ldots,D/2\}\), \(D=N-1\).
Define the two exact one-vertex functions
\[
 \begin{split}
 W_{n,N}(x)&=\phi_N[R^n\mathbf B_N(x)K_N(\,\cdot\,,0)],\\
 U_{n,N}^{[T]}(x)&=
       \phi_N^{\rm out,T}[R^n\mathbf B_N(x)K_N(\,\cdot\,,0)] .
 \end{split}
 \tag{16}
\]
The second trace is the original sum of physical residues
with \(|t_a|\ge T_N\), where \(T_N\) is an exact midpoint cut
converging to \(T\) from above. It keeps each first normal
together with its physical root. Put
\(W_{n,N}^{[T]}=W_{n,N}-U_{n,N}^{[T]}\).

Let \(m(T)\) be the real Newton maximum from (6)–(7) of the
[combined reduction](research_internal_pair_combined_contour_reduction.md).
The original values at \(x=j/N\), for every \(0\le j<N\),
satisfy
\[
 \begin{split}
 |U_{n,N}^{[T]}(j/N)|&\le C N^A e^{N(m(T)+\Psi(T))},\\
 |W_{n,N}(j/N)|&\le C N^A e^{3NM_\infty/2}.
 \end{split}
 \tag{17}
\]
Indeed the first Newton factor has interval rate \(m(T)\)
on the removed angular interval, and (5) bounds its complete
outside factor at rate \(\Psi(T)\). Markov's inequality on
that interval bounds their product's original normals.
Fixed crossing powers and the original trace cost polynomial
factors. The second estimate uses the corresponding full real
interval bounds \(m(0)=M_\infty/2\) and \(M_\infty\).
For high Newton indices the radical interval norm is polynomial,
so (17) includes those samples too.

An exact half-band function \(f\) has \(N\) Fourier coefficients,
each bounded by \(\max_{0\le j<N}|f(j/N)|\), by its discrete
Fourier inversion. Therefore
\[
 \sup_{\xi\in\mathbb R}|f(\xi+iY)|
       \le N e^{\pi D|Y|}\max_j|f(j/N)|.
 \tag{18}
\]
This formula holds at both parities, including the half-integer
frequencies at even \(N\). Apply it separately to each function
in (17), before multiplying.

**Theorem 3.** There is a fixed \(T<\pi\), independent of the
fixed pair powers \(n,p\ge3\), such that on the entire shifted
circle at its actual height,
\[
 \sup_{0\le\xi\le1}
 \left|W_{n,N}(\xi+iY)W_{p,N}(\xi+iY)
       -W_{n,N}^{[T]}(\xi+iY)W_{p,N}^{[T]}(\xi+iY)\right|
       \le C N^A e^{N(M_{n,p}-1/100)} .
 \tag{19}
\]
All original physical normals are included, through both
level parities.

*Proof.* The difference is
\(U_nW_p+W_nU_p-U_nU_p\). Equations (17)–(18) bound its first
two terms by rate
\[
        \frac32M_\infty+2\pi Y+m(T)+\Psi(T).
 \tag{20}
\]
Choose \(T\) sufficiently close to \(\pi\) that
\(m(T)+\Psi(T)<1/100\). This is possible by (6) and
\(m(T)\to0\). The double-omitted term has an even smaller
bound. Lemma 2 and \(M_\infty<7/6\), proved by the rational
Catalan-series comparison in Section 4 of the
[first-normal region note](research_pair_triangular_normal_region.md), give
\[
 \frac32M_\infty+2\pi Y+m(T)+\Psi(T)
               <\frac74+\frac34+\frac1{100}=\frac{251}{100}.
 \tag{21}
\]
The [positive power contraction and geometric action bound](research_pair_triangular_normal_region.md#3-the-two-first-normal-factors-are-below-the-geometric-rate)
give \(M_{n,p}\ge M_{3,3}>63/25=252/100\).
This proves (19). \(\square\)

The exact circle identity multiplies the integral of this
difference by \(N\), which only changes its polynomial factor.
Thus Theorem 3 removes these original angular rows even after
the shared wire is shifted to its actual geometric height.
It does not bound a folded angular connector merely by naming
it an omitted row: such a connector must be estimated in its
exact contour representation or grouped with the whole
one-vertex source.

The product in (19) has up to \(2N-1\) integer frequencies.
Its \(N\) samples would not determine it. The separate
half-band reconstructions (18) are essential to the argument.
The complete-boundary hypothesis is also retained throughout;
no off-spectrum norm bound has been inferred from ordinary
colored invariants.


## 4. Exact scalar record

The [focused checker](../experiments/check_internal_pair_angular_tail_transport.py)
verifies the rational bounds in (12), (14), (15), and (21).
Its [saved record](../repro/results/research-internal-pair-angular-tail-transport.json)
records the proof and direct dependency hashes. These scalar checks
do not replace the recurrence, interpolation, or contour proofs above.
