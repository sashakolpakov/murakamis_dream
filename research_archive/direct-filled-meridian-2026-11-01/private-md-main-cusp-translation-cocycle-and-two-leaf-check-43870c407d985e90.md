# Main-cusp translations from the original face maps

Private mathematical derivation, 1 November 2026. The general preferred-longitude identity remains open. This note proves an exact local translation table and the complete two-leaf pure case. Neither conclusion is inferred from the quantum asymptotic.

## 1. The question and the fixed normalization

The filled-source calculation, after its exact reduced-cut and scalar factors are removed, has first correction
\[
 -\frac{\pi s^2}{N}\sum_e\cot(\pi x_e^{\mathrm{fill}}).
 \tag{1}
\]
If the retained scalar ratio is \(q^{A s^2/2}\), with \(q=e^{\pi i/N}\), then putting \(z=2\pi i s\) rewrites the full quadratic coefficient as
\[
 \frac{z^2}{8\pi iN}
 \left(A+2i\sum_e\cot(\pi x_e^{\mathrm{fill}})\right).
 \tag{2}
\]
This algebraic rewriting does not identify the parenthesis with a preferred cusp shape. Such an identification requires the actual main meridian and preferred longitude, including the effect of the original framing and auxiliary fillings.

The geometric inputs below are the actual face maps in notes/actual_conway_general_mask_marked_filling.md, Sections 4–6, and the literal segment connections in notes/actual_conway_bowtie_projection_cut.md, Sections 2–4. They already give a representation of the original group. In particular, the two white maps adjacent to each main corner are actual final white transitions, even when one began as a completion map at an open leaf.

## 2. Coordinates in which the small meridian is a unit translation

In the normalized ordered quadrilateral
\[
 (C_0,C_1,C_2,C_3)=(0,\infty,1,R),\qquad E=e^{2\pi i x},
\]
the four white maps are
\[
\begin{split}
 W_0&=\begin{pmatrix}1&0\\0&E\end{pmatrix},
 &W_1&=\begin{pmatrix}1&E-1\\0&E\end{pmatrix},\\
 W_2&=\begin{pmatrix}E-R&R(1-E)\\E-1&1-ER\end{pmatrix},
 &W_3&=\begin{pmatrix}R&0\\1-E&ER\end{pmatrix}.
\end{split}
\tag{3}
\]
All matrices are projective. Put \(m_j=W_{j-1}^{-1}W_j\), with indices modulo four, and choose the alternating local orientation
\[
                         \mu_j=m_j^{(-1)^j}.
\tag{4}
\]
These choices are local. An oriented main component must still transport its meridian consistently through turns and segment identifications; (4) is not an assertion that every corner independently has the global preferred orientation.

The following coordinates send the respective corner to infinity:
\[
\begin{split}
 \xi_0(z)&=\frac{ER}{(E-1)z},
 &\xi_1(z)&=-\frac{z}{E-1},\\
 \xi_2(z)&=-\frac{E(R-1)}{(E-1)(z-1)},
 &\xi_3(z)&=-\frac{R(R-1)}{(E-1)(z-R)}.
\end{split}
\tag{5}
\]
Direct multiplication of (3) proves
\[
                    \xi_j\mu_j\xi_j^{-1}(w)=w+1.
\tag{6}
\]
The denominators are nonzero on the selected strict complete branch and hence in a sufficiently small deformation neighborhood.

The pure shaded map and the two odd maps are
\[
 S=\begin{pmatrix}0&-ER\\1&-1-E\end{pmatrix},\quad
 A=\begin{pmatrix}R&-R\\1&ER-1-E\end{pmatrix},\quad
 B=\begin{pmatrix}R/E-1-1/E&R\\-1&R\end{pmatrix}.
\tag{7}
\]
For the second projection ball, put \(\xi_j^-=\xi_j|_{E\mapsto E^{-1}}\). Here the substitution specifies the analytically continued second chart, not an antiholomorphic operation on a complex deformation parameter. The exact affine transports are
\[
\begin{array}{c|c|c}
\text{map}&\text{corner transport}&\text{translation in the indicated }\xi\text{ coordinates}\\ \hline
S&1\longrightarrow0&(E+1)/(E-1)\\
S&2\longrightarrow3&(R-1)/(E-1)\\
A&1^+\longrightarrow3^-&-(ER-E-1)/(E-1)\\
A&2^+\longrightarrow0^-&-1/(E-1)\\
B&3^+\longrightarrow1^-&(E-R+1)/(E-1)\\
B&0^+\longrightarrow2^-&-E/(E-1).
\end{array}
\tag{8}
\]
Every affine multiplier in this table is one. For example the first row means
\(\xi_0S\xi_1^{-1}(w)=w+(E+1)/(E-1)\).
This gives actual translations, not just equal derivatives at a fixed point.

The corresponding white maps have multiplier minus one between these local choices of orientation:
\[
\begin{array}{c|cc}
 &\text{first incident corner}&\text{second incident corner}\\ \hline
W_0&(0:\ -w)&(1:\ -w)\\
W_1&(1:\ -w+1)&(2:\ -w)\\
W_2&(2:\ -w-1)&(3:\ -w-R)\\
W_3&(3:\ -w+1-R)&(0:\ -w+1).
\end{array}
\tag{9}
\]
For example these are the maps \(\xi_j^-W_i\xi_j^{-1}\). Thus one cannot simply sum every displayed translation without transporting the oriented meridian. An inverse map or an orientation change contributes its actual affine sign.

## 3. The exact translation-cocycle rule

This rule applies to any of the existing deformed face-pairing representations. Let a peripheral path visit flags \(P_0,\ldots,P_\ell=P_0\). Choose a coordinate \(u_j\) at each flag that sends its consistently oriented small meridian to \(w\mapsto w+1\). Let \(F_j\) be the actual face or chart transition from \(P_{j-1}\) to \(P_j\). The original edge relations imply
\[
                  F_j\mu_{j-1}F_j^{-1}=\mu_j.
\tag{10}
\]
Consequently \(u_jF_ju_{j-1}^{-1}\) commutes with the unit translation, and is itself a translation \(w\mapsto w+\beta_j\). The translation of the entire path is exactly
\[
                              \sum_{j=1}^{\ell}\beta_j.
\tag{11}
\]
Indeed, the coordinate changes cancel in the ordered product, and translations add. Changing a coordinate origin by \(u_j\mapsto u_j+a_j\) changes \(\beta_j\) by \(a_j-a_{j-1}\), whose sum is zero.

At a pure shaded transition, one may center both coordinates at its auxiliary apex. The shaded map fixes that apex and intertwines the oriented meridians, so its translation in the centered coordinates is zero. The odd shaded map sends the selected apex to its second-ball apex; centering at those two actual flags gives the same conclusion. This moves the translation contributions to the changes between the two apex decorations at an actual main segment. It does not remove them.

Equations (5)–(11), together with the explicit prism, turn and root chart maps, give a finite exact algorithm for any specified peripheral word. The outstanding general step is to prove that the preferred main-longitude sum reduces to the retained-edge expression in (2), with the same integer \(A\) as the full quantum scalar ledger. The fact that all main meridians are parabolic proves neither that reduction nor its integer part.

## 4. A complete calculation for the strict two-leaf pure closure

Consider the literal closure \(C(h\,T(h))\), with both leaves pure before their integral disk fillings. The two leaf labels agree; write their common value as \(x\), and put \(E=e^{2\pi i x}\). The first normalized quadrilateral has parameter \(R\), and the second has parameter \(1-R\). This is the actual turn and closing constraint, valid throughout the small auxiliary deformation, not just at completeness.

Use the first leaf as world chart. The second leaf is placed by the actual quarter-turn and final reverse-order closing maps:
\[
 T_G(z)=\frac{-R}{z-1},\qquad
 C_F(z)=\frac{z-R}{z-1},\qquad
 J=C_FT_G=
 \begin{pmatrix}-R&0\\-1&1-R\end{pmatrix}.
\tag{12}
\]
Hence its corners match the first leaf's corners as
\[
 G_0=F_0,\quad G_1=F_3,\quad
 G_2=F_2,\quad G_3=F_1.
\tag{13}
\]
The pure shaded maps in their own charts are
\[
 S_F=\begin{pmatrix}0&-ER\\1&-1-E\end{pmatrix},\qquad
 S_G=\begin{pmatrix}0&-E(1-R)\\1&-1-E\end{pmatrix},
\qquad \widetilde S_G=JS_GJ^{-1}.
\tag{14}
\]

Follow the main component from \(F_0\). Its consecutive puncture crossings and identity segments are
\[
 F_0\xrightarrow{S_F^{-1}}F_1=G_3
 \xrightarrow{\widetilde S_G^{-1}}G_2=F_2
 \xrightarrow{S_F}F_3=G_1
 \xrightarrow{\widetilde S_G}G_0=F_0.
\tag{15}
\]
The four segment vertices are distinct. This path traverses the main component exactly once, and the actual peripheral word is
\[
                    L=\widetilde S_GS_F\widetilde S_G^{-1}S_F^{-1}.
\tag{16}
\]
It is a longitude rather than a meridian multiple: its projection follows the main component once. It is preferred because (16) is a commutator, so its homology class is zero in the augmented link exterior. After any of the indicated auxiliary disk fillings it still has zero homology, since the image of a commutator remains in the commutator subgroup. The image of the path remains a single longitudinal traversal of the unfilled main cusp. Thus no unknown integral meridian correction is present in this case.

Conjugate (16) by the coordinate \(\xi_0\) from (5). Matrix multiplication using (12)–(14) gives, for independent nondegenerate \(E,R\),
\[
 \xi_0L\xi_0^{-1}
 =\begin{pmatrix}
 1&-2(E+1)/(E-1)\\0&1
 \end{pmatrix}.
\tag{17}
\]
The meridian is the unit translation by (6). Since
\[
                    \frac{E+1}{E-1}=-i\cot(\pi x),
\]
the preferred main-cusp shape is exactly
\[
                         \boxed{\tau_{\mathrm{main}}=2i\cot(\pi x).}
\tag{18}
\]
At completeness \(x=1/4\), so the orientation has positive imaginary shape \(2i\). Formula (18) continues along the original small auxiliary deformation and hence on every sufficiently long pure filling branch supplied by the marked filling theorem. The two-leaf contraction has one retained turn edge, whose wire coordinate is this same \(x\). Therefore its geometric cotangent term is exactly the one in (1), with no additional integer in the preferred longitude.

This calculation does not determine the full quantum scalar ledger for the two-leaf presentation. It supplies an independent geometric target for that ledger. Nor does it establish the general tree identity or the odd-pattern integer correction.

## 5. Remaining general obligations

For a general strict tree, a proof of (2) as a cusp shape needs three additional exact steps.

1. Compile the main component's preferred longitudinal path from the original ribbon cut, including the copy switches at odd shaded gluings. The diagram-framed path must be corrected by its actual meridian power when necessary.
2. Transport the unit meridian frames through every original prism, turn and closing identification. Sum the affine translations by (11), and prove the cancellation of hidden unturned resolution variables. Individual quadrant translations in (8) depend on \(R\), so this cancellation is a substantive identity.
3. Compare the remaining integral contribution with the complete carrier, crossing and zero-framing ledger. Scalar normalization alone does not choose a peripheral longitude, and local parabolicity alone does not fix an additive integer in its translation.

The existing filled-volume proof does not need any of these further identifications: its absolute action and auxiliary primitive filling equations have already been calibrated independently.
