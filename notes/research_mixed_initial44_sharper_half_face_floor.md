# A sharper original half-face floor for an initial four/four cap

Private written deduction, 10 November 2026. At an actual initial
four/four reference, the original bare cap marginal is greater
than \(-1/3\). Consequently the already used allocated half-face
plane is greater than \(183/200\). This improves its former
\(149/200\) floor without evaluating an action or changing its
normalization.

This is a floor for the original comparison plane. It is not a
new finite-source upper bound for a contour or an added height
connector.

## 1. Original reference and action

Fix an actual positive three/four open word of length at least
three beginning with four and four. The exact reference boxes
from [the first-four/four last-row theorem](research_mixed_first_four_four_true_last_row_calibration.md)
are
\[
 a_*=a_0+ic,\quad e_*=u_*+ih_*,
 \quad .246<a_0<.350,\quad -.078<c<-.020,
 \quad .333<u_*<.363,\quad -.051<h_*<-.019.
 \tag{1}
\]
They refer to the original coupled reference, not an arbitrary
substitution into a critical equation.

Keep the bare cap action from
[the complete first-cap packet](research_mixed_complete_first_cap_packet.md),
\[
 T(a)=\mathcal T_1(a,-2)
 =\Psi_1(e_*(a),a,-2),\qquad
 \Psi_1(e,a,-2)=S(e)+J(e+a)-J(a)-i\pi ea-g(e).
 \tag{2}
\]
Here \(J(0)=0\), \(J'=\Log(2\sin\pi\cdot)\), and
\(g(z)=J(z)+i\pi(z-z^2)/2\), on the original strip branches.
That theorem, Section 3, equation (12), proves at the entire
actual endpoint image
\[
                              \Re T(a_*)>1.
 \tag{3}
\]
Its definition (2) is the phase of the literal
\[
 U_{1,N}(w,X)=\sum_{j=0}^{N-1}
 H_N(w,q_N^{-j})\frac{(q_NX;q_N)_j}{(q_N;q_N)_j^2}.
 \tag{4}
\]
Here \(q_N=e^{-2\pi i/N}\), exactly as in that finite-source theorem.
In particular (3) is before allocation of an outgoing Fourier
halfweight. It is not a claim about the allocated action
\(L_1=T-g/2\).

For \(\kappa=1/2500000\), define exactly the two planes used by
[the lower-right cap theorem](research_mixed_first_four_cap_lower_right_horizontal.md):
\[
\begin{split}
 B_T&=\Re T(a_*)+\Re T'(a_*)(1/2-a_0)
                         -\kappa(1/2-a_0)^2,\\
 B_*&=\Re L_1(a_*)+\Re L_1'(a_*)(1/2-a_0)
                         -\kappa(1/2-a_0)^2.
\end{split}
 \tag{5}
\]

## 2. A lower bound on the actual bare marginal

Stationarity in \(e\) gives the exact marginal, also retained in
Section 6 of [the plateau phase proof](research_mixed_first_cap_plateau_phase.md):
\[
 T'(a_*)=J'(a_*+e_*)-J'(a_*)-i\pi e_*
                         =g'(a_*+e_*)-g'(a_*).
 \tag{6}
\]
Thus no chirp is omitted in the modulus calculation below.
Put
\[
 r=e^{2\pi c},\qquad q=e^{2\pi h_*},\qquad
 N_e=|1-rq e^{-2\pi i(a_0+u_*)}|,\qquad
 D=|1-r e^{-2\pi ia_0}|.
 \tag{7}
\]
Then \(\Re T'(a_*)=\log(N_e/D)\).

The actual height bounds imply
\[
                       0<r<\frac9{10},\qquad q>\frac{18}{25}.
 \tag{8}
\]
For the first assertion, \(\log(10/9)<1/9<\pi/25\), whereas
\(-2\pi c>\pi/25\).
For the second,
\[
 \log(25/18)=2\operatorname{artanh}(7/43)
 >\frac{14}{43}>\frac{561}{1750}>\frac{51\pi}{500};
 \tag{9}
\]
the middle cross-product difference is \(377>0\).
Use \(2\pi h_*>-51\pi/500\).

The real reference boxes give
\[
             \cos 2\pi(a_0+u_*)<-\frac15,\qquad
                         \cos 2\pi a_0>-\frac35.
 \tag{10}
\]
For the first bound, \(a_0+u_*\in(.579,.713)\), so its
largest cosine is at the upper end and is
\(-\sin(37\pi/500)<-1/5\).
For a direct rational sine witness, \(37\pi/500>21/100\)
and \(37\pi/500<1/4\); hence
\(\sin(37\pi/500)>21/100-(1/4)^3/6>1/5\).
For the second bound, the smallest cosine occurs at \(a_0=.35\)
and equals \(-\sin(\pi/5)>-3/5\), by the exact half-angle
formula.

It follows from (7)--(10) that
\[
 N_e^2>1+\frac{324}{625}r^2+\frac{36}{125}r,\qquad
                  D^2<1+r^2+\frac65r .
 \tag{11}
\]
Consequently
\[
 16N_e^2-9D^2
 >7-\frac{441}{625}r^2-\frac{774}{125}r
 >\frac{53479}{62500}>0.
 \tag{12}
\]
The quadratic on the middle right decreases for \(r\ge0\);
its value at \(9/10\) is the displayed rational number.
Therefore
\[
                 \Re T'(a_*)>\log(3/4)>-\frac13,
 \tag{13}
\]
where the last inequality is \(\log(1+1/3)<1/3\).

## 3. The bare and allocated half-face floors

Since \(0<1/2-a_0<127/500\), equations (3), (5), and (13)
give
\[
 B_T>1-\frac{127}{1500}-\kappa
     =\frac{1373}{1500}-\kappa>\frac{183}{200}.
 \tag{14}
\]
The last unused reserve before the \(\kappa\) subtraction is
\(1/3000>\kappa\).

The allocated comparison is the same one used in the earlier
lower-right theorem. Along the actual-height horizontal interval
from \(a_*\) to \(1/2+ic\),
\(\Re g''=\pi\Re\cot\pi a\ge0\), and
\(\Re g(1/2+ic)=0\).
Its tangent at the original reference therefore satisfies
\[
 \Re\{g(a_*)+g'(a_*)(1/2-a_0)\}\le0.
 \tag{15}
\]
Subtracting one half of (15) in (5) proves
\[
                   \boxed{\quad B_*\ge B_T>\frac{183}{200}.\quad}
 \tag{16}
\]

All actions, logarithmic lifts, and allocations are unchanged.
The deduction uses the previously proved original action floor
(3) and elementary inequalities only. It does not calculate a
new action value, enlarge a finite-source domain, or pay an
uncalibrated complementary contour merely because its floor
has improved.

## Frozen source bindings

| Direct source | SHA-256 |
|---|---|
| research_mixed_complete_first_cap_packet.md | 245e3c90a322ad094466c082bdf79f4234c68bb6a4ee98af356d650907ee5f1b |
| research_mixed_first_cap_plateau_phase.md | 159a1b89eebcb72fa9ac3395435086f066b3e648c389e2417e0b61fb490ff612 |
| research_mixed_first_four_four_true_last_row_calibration.md | 52c149d8500e88c6e4e3fdf1c9e699baf376dfaac8b96d3461dc81f9d1725e0d |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
