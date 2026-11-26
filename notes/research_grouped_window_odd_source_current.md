# The actual odd source and one grouped window current

Private written proof, 19 November 2026.

The whole unmarked braid source is an exact odd-meridian extraction
from one sample of its integer-degree trace. For an arbitrary analytic
marked matrix, the same extraction has one explicit correction. It is
the sum of a return-window current and the forced total-
\(E\) source current. Their possible simple meridian poles cancel;
the grouped correction is holomorphic. Its value is given below by
one complete first-normal packet.

The point is to identify the actual current that a geometric-window
comparison would have to estimate. No geometric estimate, selection
of a relative cycle, or nonzero closed contribution is asserted.
The complete directs are J and F, pinned at the end. J already proves
graded reciprocity and the return defect; F already proves the forced
source formula. The new consolidation retains both in the same odd
extraction, rather than treating a marked window as an intertwiner.

## 1. The original source and the actual return

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(m\ge2\), and \(r=m-1\). Put
\[
 M=e^\mu,\quad x=-M/q,\quad c=(-q^{-1})^r,
 \qquad \varepsilon=c^N=(-1)^{(N+1)r}.
 \tag{1}
\]
All derivatives hold this quantum root and the physical occupation
bases fixed. Let \(J_0\) be total integer occupation on the remaining
\(r\) heads; it has values \(0,\ldots,rd\), not residues modulo \(N\).
Write \(U_j=\ker(J_0-jI)\) and \(P_0=|0\rangle\langle0|\) on the
first physical head.
The remaining Cartan is
\[
 K_{\rm r}(\mu)=e^{r\mu}cQ^{-J_0},\qquad
 g(\mu)=K_{\rm r}(\mu)^{1-N}.
 \tag{2}
\]
Use the actual prefix maps of J and F,
\[
 q_F(\mu)=p_0S_m(e^\mu)^{-1},\qquad i_F=i_0,
 \qquad q_Fi_0=I,\quad q_FF_\Sigma=0.
 \tag{3}
\]
They are analytic at zero. For an arbitrary analytic full-head
matrix \(A_\mu\), set
\[
 C_A(\mu)=q_F(\mu)A_\mu i_0,\qquad
 \Phi_A(\mu)=\operatorname{Tr}((P_0\otimes g(\mu))A_\mu).
 \tag{4}
\]
The original \(\Phi_A\) is analytic. The matrix \(A\) may be a
literal word with partial coherent resolutions or other finite
marks. No total-arrow intertwining is imposed on those marks.

Choose an actual unmarked braid family \(W_\beta(\mu)\), with J's
crossing and framing conventions, and let
\(B_\mu=q_F W_\beta(\mu)i_0\). It is analytic, invertible, and
preserves \(J_0\). This is a reference word for describing a window;
the scalar formulas below do not depend on its choice.

Let \(V_\mu\) be the actual reduced half-twist used in J(30b), with
\[
 B_{\beta^{\rm rev}}(\mu)=V_\mu B_\mu V_\mu^{-1}.
\]
It is analytic, invertible, and degree preserving. J's literal return
is \(T(\mu)=q_F E_\Sigma^d\mathscr C i_F(e^{-\mu})\). Define
\[
 \mathscr R_\mu=T(\mu)V_{-\mu}.
 \tag{5}
\]
J(11),(30a) give the exact whole-meridian identities
\[
 B_\mu\mathscr R_\mu=\mathscr R_\mu B_{-\mu},\qquad
 \mathscr R_\mu U_j\subset U_{rd-j},\qquad
 Q^{-J_0}\mathscr R_\mu=Q^r\mathscr R_\mu Q^{J_0}.
 \tag{6}
\]
The last factor is \(Q^{-rd}=Q^r\), with \(d=N-1\) retained.
The return is analytic and generically invertible near zero; its
inverse is used only on a punctured disk and then by meromorphic
continuation. J's exact product supplies that inverse. No coherent
symbol or geometric window transport is being inferred from (6).

## 2. The scalar return current is removable

First let \(P_\mu\) be any analytic matrix on the remaining space.
It need not preserve degree or be an idempotent. Its actual return
defect and the corresponding scalar are
\[
 \Delta_P(\mu)=P_\mu\mathscr R_\mu-
                         \mathscr R_\mu P_{-\mu},
 \qquad
 \delta_P(\mu)=\operatorname{Tr}
   \bigl(Q^{-J_0}\Delta_P(\mu)\mathscr R_\mu^{-1}B_\mu\bigr).
 \tag{7}
\]
This is J's two-window defect with the half-twist transported on
the reflected window. Cyclicity, (6), and the finite matrix inverse
give
\[
 \boxed{\quad
 \delta_P(\mu)=
 \operatorname{Tr}(Q^{-J_0}P_\mu B_\mu)
       -Q^r\operatorname{Tr}(Q^{J_0}P_{-\mu}B_{-\mu}).
 \quad}\tag{8}
\]
Indeed insert \(P_\mu=\mathscr R_\mu P_{-\mu}\mathscr R_\mu^{-1}
+\Delta_P\mathscr R_\mu^{-1}\), and use
\(\mathscr R_\mu^{-1}Q^{-J_0}\mathscr R_\mu=Q^rQ^{J_0}\).
Both traces on the right are analytic. Thus the scalar (7) has a
removable singularity, even when its displayed inverse has a pole.
This does not make the matrix defect vanish.

For the full marked matrix (4), use its exact effective window
\[
 P_{A,\mu}=C_A(\mu)B_\mu^{-1},\qquad
 \delta_A=\delta_{P_A},\qquad
 f_A(\mu)=e^{-m\mu}\operatorname{Tr}(Q^{J_0}C_A(\mu)).
 \tag{9}
\]
These are analytic. Formula (8) shows that \(\delta_A\), like
\(f_A\), is independent of the reference braid and half-twist.
Their role in (7) is to expose the actual return-window comparison.

There is a useful guard when \(A_\mu=\Pi_\mu W_\beta(\mu)\).
F supplies the literal partial inverse
\(I-i_0q_F=F_\Sigma\Lambda_F\). It gives
\[
 P_{A,\mu}=q_F\Pi_\mu i_0
   +q_F[\Pi_\mu,F_\Sigma]\Lambda_F
                          W_\beta(\mu)i_0B_\mu^{-1}.
 \tag{10}
\]
To prove this, expand \(W_\beta i_0=i_0B+F_\Sigma\Lambda_FW_\beta i_0\)
and use \(q_FF_\Sigma=0\). Thus the effective window cannot be
replaced by \(q_F\Pi i_0\) without its displayed \(F\)-current.

## 3. Exact odd extraction and the grouped correction

Write
\[
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}},\qquad
 H(\mu)=D_N(e^\mu K_{\rm r}(\mu)),\qquad
 L_N(\mu)=\frac{D_N(e^\mu)}{2\varepsilon\sinh(mN\mu)}.
 \tag{11}
\]
The Laurent-polynomial continuation defines \(D_N\) at \(\pm1\).
On a sufficiently small punctured disk, direct use of (2) gives
\[
 D_N(e^\mu)\operatorname{Tr}(H^{-1}C_A)
 =L_N(\mu)\left[
  ce^{m\mu}\operatorname{Tr}(Q^{-J_0}C_A(\mu))
  -c^{-1}e^{-m\mu}\operatorname{Tr}(Q^{J_0}C_A(\mu))\right].
 \tag{12}
\]
This uses the finite physical identity \(K_0^N=\varepsilon I\).
No off-grid clock power is substituted. Since \(cQ^r=c^{-1}\),
(8)--(9) turn (12) into
\[
 \mathscr O_A(\mu)+ce^{m\mu}L_N(\mu)\delta_A(\mu),
 \qquad
 \mathscr O_A(\mu)=c^{-1}L_N(\mu)
                         \bigl(f_A(-\mu)-f_A(\mu)\bigr).
 \tag{13}
\]
The odd numerator makes \(\mathscr O_A\) analytic at zero.

F(14f)--(14g) constructs a fixed meromorphic matrix
\(\mathcal W_E(\mu)\), independent of \(A\), such that
\[
 \Phi_A(\mu)=D_N(e^\mu)\operatorname{Tr}(H^{-1}C_A)
       +\operatorname{Tr}(\mathcal W_E(\mu)Y_A(\mu)),
 \qquad Y_A=[E_\Sigma,A_\mu].
 \tag{14}
\]
Its pole at zero has order at most one. It includes the original
highest cut and \(g\), not a substituted ordinary trace.

Define the grouped current by its explicit two terms:
\[
 \boxed{\quad
 \mathcal G_A(\mu)=ce^{m\mu}L_N(\mu)\delta_A(\mu)
                +\operatorname{Tr}(\mathcal W_E(\mu)Y_A(\mu)).
 \quad}\tag{15}
\]
Then
\[
 \boxed{\qquad \Phi_A(\mu)=\mathscr O_A(\mu)+\mathcal G_A(\mu).
 \qquad}\tag{16}
\]
Both terms in (15) may have a simple pole, but their sum is
holomorphic: (14) is the original analytic finite source and
\(\mathscr O_A\) is analytic. This proves removal for the grouped
current, without setting either residue to zero separately.
One can choose a disk \(|\mu|<b/N\), \(0<b<\pi/m\), small enough
for all specified analytic families; no other zero of the displayed
\(\sinh(mN\mu)\) lies there. No uniform norm bound follows.

For \(A=W_\beta\), the effective window is \(I\), so
\(\Delta_P=\delta_A=0\), and \(Y_A=0\) by actual intertwining.
Thus \(\mathcal G_{W_\beta}=0\) and (16) is the full unmarked
odd-source formula. Equivalently, if
\(T_\beta(s,M)=\operatorname{Tr}(s^{J_0}B(M))\), then
\[
 f_{W_\beta}(\mu)=e^{-m\mu}T_\beta(Q,e^\mu),\qquad
 \Phi_{W_\beta}(\mu)=
 \frac{c^{-1}\sinh(N\mu)}
 {2\varepsilon\sinh\mu\sinh(mN\mu)}
       \bigl(f_{W_\beta}(-\mu)-f_{W_\beta}(\mu)\bigr).
 \tag{17}
\]
The whole trace reciprocity behind this specialization is J(30b).
Equation (16), unlike this unmarked specialization, retains the
actual currents for a window.

## 4. The complete first-normal packet

Use the fixed coordinate \(\mu=\log M\), and write
\[
 \mathcal W_E(\mu)=U_{-1}/\mu+U_0+O(\mu).
 \tag{18}
\]
Since \(D_N(e^\mu)\) is even and has value \(N\),
\[
 L_N(\mu)=\frac1{2\varepsilon m\mu}+O(\mu).
 \tag{19}
\]
The vanishing residue of (15) is precisely
\[
 \boxed{\quad
 \frac{c}{2\varepsilon m}\delta_A(0)
                    +\operatorname{Tr}(U_{-1}Y_A(0))=0.
 \quad}\tag{20}
\]
Its value and the original source are
\[
 \boxed{\begin{split}
 \mathcal G_A(0)
  &=\frac{c}{2\varepsilon m}
          \bigl(\delta_A'(0)+m\delta_A(0)\bigr)
     +\operatorname{Tr}\bigl(U_{-1}Y_A'(0)+U_0Y_A(0)\bigr),\\
 \Phi_A(0)&=-\frac{c^{-1}}{\varepsilon m}f_A'(0)
                                      +\mathcal G_A(0).
 \end{split}}\tag{21}
\]
All derivatives are genuine fixed-\(q\) meridian derivatives.
They include the prefix, return, half-twist, total arrow, window,
word, and any moving frames actually used to define those matrices.
Formula (8) computes \(\delta_A'\) using only analytic finite blocks,
without differentiating the singular inverse in (7).

In particular
\[
 Y_A'(0)=[E_\Sigma'(0),A_0]+[E_\Sigma(0),A_0'],
 \quad
 f_A'(0)=\operatorname{Tr}Q^{J_0}
 \bigl(q_F'(0)A_0i_0+q_F(0)A_0'i_0-mC_A(0)\bigr).
 \tag{22}
\]
Changing \(A_0'\) while fixing \(A_0\) leaves the original
\(\Phi_A(0)\) unchanged, but need not leave the odd term unchanged.
For a change \(A_0'\mapsto A_0'+Z\), (21) gives exactly
\[
 \Delta\mathcal G_A(0)=\frac{c^{-1}}{\varepsilon m}
                   \operatorname{Tr}(Q^{J_0}q_F(0)Zi_0).
 \tag{23}
\]
Thus a chosen window's meridian extension is part of the comparison.
It cannot be replaced by its root value before the two currents are
combined. This also guards against assigning a local odd normal from
root trace reciprocity alone.

Every prescribed outside scalar line \(\Xi_N(\mu)\) multiplies
the entire equality (16). For an analytic line, the finite part of
each unresolved term of (15) contains its \(\Xi_N'(0)\) times
that term's residue. These additions cancel by (20), leaving
\(\Xi_N(0)\mathcal G_A(0)\). A meromorphic line instead retains
its full prescribed Laurent multiplication. No scalar normalization
or zero-framing derivative is dropped.

## 5. What the identity asks of a geometric comparison

J's partial coherent resolutions are actual finite matrices, so
analytic families of such windows fit (7). Likewise full-head marked
windows fit (4) with their forced rows retained. Formula (10) records
the difference between these two placements. No pointwise product of
normalized coherent symbols is used.

The exact correction to the odd extraction is the single analytic
quantity \(\mathcal G_A\). Its packet (21) is what must be compared
with any independently established localized geometric odd period.
Neither the nonzero local density of a literal factorial interpolant
nor equality of rational canonical graphs bounds this quantity.
The two total-eigenflag choices are not identified with two partial
resolutions by (6), and the finite integer-degree reflection is not
an interpolation at a complex geometric occupation.

No geometric asymptotic, half-density transport, negligible current,
or original-cycle coefficient is a hypothesis renamed as a conclusion
here. Complementary windows, incidence-boundary currents and all
physical caps remain. The result is the exact grouped source row
(15)--(21), including its forced meridian cancellation.

## Complete proof directs

* J: `notes/research_opposite_polarization_source_kernel.md` (639 lines),
  SHA256 `d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44`.
* F: `notes/research_forced_source_and_opposite_kernel_transport.md`
  (603 lines), SHA256
  `2e92bab4e3c510519098e3a10ed4227a8f4b492393b3742d02e4fdcaa3cca0f5`.

Both complete matching directs were freshly whole-read nontruncated
in this active author sequence. Every used implication was checked.
The calculations above are finite written matrix and Laurent
identities. No mathematical programs, tests, builds, or changes to
frozen or public files were used.
