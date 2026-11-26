# The all-circle edge equation as a marked four-punctured-sphere character

Private derivation, 1 November 2026.

This report gives explicit matrices for the new all-circle effective edge equation. The construction retains the main eigenvalue, both auxiliary eigenvalue ratios, and a main-longitude commutator. It does not yet identify its abstract four-puncture generators with every original octahedral face path. That topological and marking comparison is stated separately in Section 6.

## 1. The source relation is linear in the internal trace

Use the actual source variables
\[
 M=e^{\pi it},\qquad E=e^{2\pi ix},\qquad
 Q=e^{i\tau_v},\qquad P=e^{i\tau_w}.
 \tag{1}
\]
The edge equation is
\[
 (E+Q)(E+Q^{-1})(E+P)(E+P^{-1})
       =(E-1)^2(1-EM^2)(1-E/M^2).
 \tag{2}
\]
Write
\[
 m=M+M^{-1},\quad D=M^2+M^{-2}=m^2-2,\quad
 \beta=Q+Q^{-1},\quad \gamma=P+P^{-1},\quad
 A_0=E+E^{-1},\quad S=\beta+\gamma+m^2.
 \tag{3}
\]
Each factor pair on the left of (2) is \(E(A_0+\beta)\) or \(E(A_0+\gamma)\). The two pairs on the right are \(E(A_0-2)\) and \(E(A_0-D)\). Dividing by \(E^2\) gives
\[
 (A_0+\beta)(A_0+\gamma)=(A_0-2)(A_0-D),
 \qquad
 A_0=\frac{2D-\beta\gamma}{S}.
 \tag{4}
\]
Near the complete point \(M=Q=P=1,E=i\), the denominator \(S\) is eight. Thus (2) is a quadratic equation for \(E\), with the selected branch through \(i\). Its apparent degree-four form contains a cancellation of the quadratic terms in \(A_0\).

## 2. A four-puncture character and its explicit matrices

Put
\[
 p=-\beta,\qquad q=-\gamma,\qquad X=2+SE,
 \qquad b=p-2,\quad h=M-M^{-1}.
 \tag{5}
\]
For the moment \(p,q,X\) may be arbitrary nearby parameters. Define
\[
 A=\begin{pmatrix}M&1\\0&M^{-1}\end{pmatrix},
 \qquad
 B=\begin{pmatrix}M^{-1}&0\\b&M\end{pmatrix}.
 \tag{6}
\]
Both have determinant one and trace \(m\), and \(\operatorname{tr}(AB)=p\). Set
\[
 c=\frac{MX+M^{-1}q-2m}{D-p},\qquad
 d=\frac{q-M^2-1+hc}{p-2},\qquad
 e=X-1-M^{-2}-hc,
 \qquad
 C=\begin{pmatrix}c&d\\e&m-c\end{pmatrix}.
 \tag{7}
\]
The denominators \(p-2=-4\) and \(D-p=4\) at the complete point are nonzero. The construction does not divide by \(M-M^{-1}\). Direct multiplication gives
\[
 \operatorname{tr}C=m,\qquad
 \operatorname{tr}(BC)=q,\qquad
 \operatorname{tr}(AC)=X,\qquad
 \operatorname{tr}(ABC)=m.
 \tag{8}
\]
For the last identity, the nonconstant part of the trace is
\(bc+Me+M^{-1}bd\), which vanishes by (7).

The determinant calculation is
\[
 \det C-1=\frac{\mathcal F(X,p,q)}{(p-2)(D-p)},
 \tag{9}
\]
where
\[
 \mathcal F=
 X^2+p^2+q^2+pqX-2m^2(p+q+X)+4m^2+m^4-4.
 \tag{10}
\]
This is the equal-boundary-trace four-punctured-sphere character equation, derived here from the matrices. For a direct verification of (9), substitute the three entries in (7), multiply by \((p-2)(D-p)\), and collect the quadratic polynomial in \(X\). Its leading coefficient is one; the other two coefficients are those displayed in (10).

Now impose (5). A direct substitution gives the especially simple identity
\[
 \mathcal F(2+SE,-\beta,-\gamma)
 =ES\bigl[(A_0+\beta)(A_0+\gamma)
                         -(A_0-2)(A_0-D)\bigr].
 \tag{11}
\]
Thus (2) is equivalent to \(\det C=1\) on this regular chart. Put
\[
                         D_0=(ABC)^{-1}.
 \tag{12}
\]
Equations (8)--(12) give
\[
 ABCD_0=I,\qquad
 \det A=\det B=\det C=\det D_0=1,\qquad
 \operatorname{tr}A=\operatorname{tr}B
       =\operatorname{tr}C=\operatorname{tr}D_0=m.
 \tag{13}
\]
These are literal matrices representing the four positively oriented boundary generators of a four-punctured sphere. Each puncture has eigenvalues \(M,M^{-1}\). In particular, the source relation is not merely similar in degree to a character equation: (7), (11), and (12) realize it by actual matrices.

At the complete selected point,
\[
 A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
 B=\begin{pmatrix}1&0\\-4&1\end{pmatrix},\quad
 C=\begin{pmatrix}-1+2i&1\\8i&3-2i\end{pmatrix}.
 \tag{14}
\]
All four punctures are noncentral parabolics. The pair \(A,B\) has no common eigenline. The construction is therefore on a regular irreducible character chart through the complete point.

The alternative root of the quadratic (10) is \(2+S/E\). Indeed its sum with \(X=2+SE\) is \(2m^2-\beta\gamma\), by (4). For comparison, its discriminant factors as
\[
 (\beta+2)(\gamma+2)
       \bigl[\beta\gamma-2\beta-2\gamma-4D-4\bigr]
           =S^2(E-E^{-1})^2.
 \tag{15}
\]
This verifies the two-sheeted parameter and its branch without assigning signs by a numerical square root.

## 3. Auxiliary transport matrices with the actual source ratios

Define two invertible projective transport matrices
\[
 V=AB+z_v I,\qquad T=BC+z_w I,
 \qquad
 z_v=-\frac{1+E(\beta+1)}{1-E},\qquad
 z_w=\frac{E+\gamma+1}{1-E}.
 \tag{16}
\]
Scalar multiples of \(V,T\) give the same projective transports. Their determinant-one normalizations can be chosen on a local square-root cover; every commutator below is independent of that choice.

The following full matrix identities hold on (2):
\[
 \begin{aligned}
 VA&=D_0^{-1}V,& VB&=C^{-1}V,\\
 TB&=A^{-1}T,& TC&=D_0^{-1}T.
 \end{aligned}
 \tag{17}
\]
They are stronger than trace matching. Also \(V\) commutes with \(AB\), and \(T\) commutes with \(BC\), directly from (16).

Here is a rational way to verify (17), preserving the regular chart. Eliminate \(\gamma\) using (4):
\[
 \gamma=\frac{2D-(E+E^{-1})(\beta+D+2)}
                         {E+E^{-1}+\beta}.
 \tag{18}
\]
The denominator is two at the complete point. Substitute (18), (5), and (7) in (17). Every difference becomes a zero rational function of \(M,\beta,E\). This is also a polynomial certificate after clearing the recorded denominators. For example, before substituting (5), the value of \(z\) solving the lower-left entry of
\((AB+zI)A=(ABC)(AB+zI)\) makes the remaining three entries scalar multiples of (10); after (5), that \(z\) reduces to \(z_v\). The other pair follows by cyclic permutation of the four punctures. No eigenline diagonalization at a repeated eigenvalue is used.

The two disk-longitude words and their selected eigenvalues are
\[
 \Lambda_v=AB,\quad \lambda_v=-Q;
 \qquad
 \Lambda_w=(BC)^{-1},\quad \lambda_w=-P.
 \tag{19}
\]
The inverse in the second word records the opposite boundary orientation. On the \(-Q\) eigenline of \(AB\), the projective eigenvalue ratio of \(V\) is
\[
 \frac{z_v-Q}{z_v-Q^{-1}}
                         =\frac{Q+E}{1+QE}.
 \tag{20}
\]
This identity follows by factoring the numerator as
\(-(1+Q)(1+E/Q)/(1-E)\) and the denominator as
\(-(1+Q^{-1})(1+EQ)/(1-E)\).

For \(T\), note \(z_w=z_v(P,E^{-1})\). Its ratio on the \(-P\) eigenline of \(BC\) is therefore the inverse of \((P+E)/(1+PE)\). The selected eigenline of \(\Lambda_w=(BC)^{-1}\) with eigenvalue \(-P\) is instead the \(-P^{-1}\) eigenline of \(BC\). Thus its marked ratio is
\[
 \frac{z_w-P^{-1}}{z_w-P}
                         =\frac{P+E}{1+PE}.
 \tag{21}
\]
Equations (20)--(21) are exactly the two source auxiliary ratios. Their extension to \(Q=P=1\) is the full matrix limit of (16), not a separate evaluation of two coalescing eigenvectors.

The determinants are nonzero nearby. More explicitly, after (18),
\[
 \begin{aligned}
 \det V&=\frac{(\beta+2)(\beta E+E^2+1)}{(E-1)^2},\\
 \det T&=
 -\frac{(E-1)^2(E-M^2)(EM^2-1)
                (\beta M^2+M^4+1)}
 {M^4(\beta E+E^2+1)^2}.
 \end{aligned}
 \tag{22}
\]
Both equal \(-4\) at the complete point. These formulas fix the regularity needed for the inverse transport matrices.

## 4. The main commutator gives the source longitude factor

Consider the ordered commutator
\[
 \Lambda_K=T V^{-1}T^{-1}V.
 \tag{23}
\]
It commutes with \(A\). This also follows from the transport paths: its inverse \(V^{-1}TVT^{-1}\) sends \(A\) successively to \(B^{-1}\), \(C\), \(D_0^{-1}\), and back to \(A\), using (17).

Set
\[
                   u=\frac{M^2-E}{1-M^2E}.
 \tag{24}
\]
The exact matrix is
\[
 \Lambda_K=
 \begin{pmatrix}
 -u & (u^{-1}-u)/(M-M^{-1})\\
 0  & -u^{-1}
 \end{pmatrix}.
 \tag{25}
\]
The apparent quotient in its upper-right entry is removable at \(M=1\). A direct certificate, without multiplying four complicated inverse matrices, is
\[
 T V=V
 \begin{pmatrix}
 -u^{-1}&(u-u^{-1})/(M-M^{-1})\\
 0&-u
 \end{pmatrix}T.
 \tag{26}
\]
Substitution of (7), (16), and (18) makes every entry of the difference zero. Multiplication by \(V^{-1}\) and \(T^{-1}\), which are legitimate by (22), gives (25). The expression for the upper-right entry is regular because \(u=1\) at \(M=1\).

The \(M\) eigenline of the positively oriented puncture \(A\) is the first coordinate line. Thus the eigenvalue of (23) on that line is \(-u\), exactly the source factor for one edge. The original source cut selects the opposite \(M^{-1}\) eigenline; its eigenvalue is \(-u^{-1}\), retaining the required inverse-flag convention.

At \(M=1\), with \(E\) kept on its continued branch,
\[
 \Lambda_K=
 \begin{pmatrix}
 -1&-2i\cot(\pi x)\\0&-1
 \end{pmatrix}.
 \tag{27}
\]
Since \(A\) translates by one, (27) has projective translation
\(2i\cot(\pi x)\). At the complete edge \(x=1/4\), this is \(2i\).
The negative SL lift in (25) is therefore compatible with the complete preferred lift; it was not inserted by multiplying the commutator by a sign.

## 5. What is realized algebraically

The matrices provide a representation of the explicitly marked transport group with four punctures \(A,B,C,D_0\), their product relation, and the two transport relations (17). Its two indicated disk longitudes are (19). Its main commuting word is (23). On this representation:

* all four main punctures have eigenvalues \(M^{\pm1}\);
* the two auxiliary disk-longitude eigenvalues are \(-Q,-P\), with the second orientation explicitly reversed;
* the two auxiliary meridian similarities are the rational source factors (20)--(21);
* the main word has eigenvalue \(-(M^2-E)/(1-M^2E)\) on the \(M\) eigenline.

The source-selected branch is the regular branch through (14). These statements are full rational matrix identities, not consequences of the common cusp tangent.

## 6. The remaining actual-topology comparison

The four-punctured sphere is an actual topological object, but an arbitrary marking of its free generators is not automatically the marking of the original Conway block. To use the construction as a geometric adapter one must identify \(A,B,C,D_0\) with the original oriented puncture paths in the two-octahedron cut, identify \(V,T\) with its actual shaded sidepairings, and verify the orientation in (19) and the four-segment word (23).

The independent geometric construction currently has exactly the same candidate commutator \(S_wS_v^{-1}S_w^{-1}S_v\) and the inverse eigenvalue on the source flag. Setting \(S_v=V,S_w=T\) is therefore consistent with its stated local word. This agreement is not yet a proof of the entire original ribbon marking, particularly for odd seams or parallel-strand orientation types. Those cases must be checked in the physical diagrams or transported by a proved marked conjugacy.

Finally, the complete matrices should be compared with the actual positive octahedral development, not merely with a representation of the same abstract group. Once that common complete marked holonomy and the full local peripheral identities are established, local rigidity can identify the selected nearby germ. Until then this report supplies the explicit character and peripheral algebra, while leaving the actual block identification as a separate requirement.

## 7. Comparison with the explicit native pure block

The new native geometric construction in
[the pure adapter](md-nonparabolic-two-octahedron-pure-adapter.md) supplies precisely the additional local data needed in Section 6 for the canonical pure two-circle block. The comparison below retains the original white-map order and uses its proved six white/shaded returns. It does not extend the marking to arbitrary odd or parallel-strand seams.

Write its four actual white maps as \(W_0,W_1,W_2,W_3\), and its two plus-copy shaded maps as \(S_v,S_w\). The equatorial corners are \(0,\infty,1,R\). Put
\[
 N_j=W_{j-1}^{-1}W_j,\qquad j\bmod4.
 \tag{28}
\]
The native corner maps have derivatives
\((M^{-2},M^2,M^{-2},M^2)\) in the finite local coordinates, with \(1/z\) at infinity. They obey
\(N_0N_1N_2N_3=I\) by literal cancellation of the white maps.

In the matrix representatives fixed in that construction,
\[
 \det W_0=L,\quad \det W_1=L/M^2,\quad
 \det W_2=L/M^4,\quad \det W_3=LM^2.
 \tag{29}
\]
The determinant-one puncture matrices to compare with (6)--(13) are therefore
\[
 A_{\mathrm g}=M^{-3}N_3,\quad
 B_{\mathrm g}=MN_0,\quad
 C_{\mathrm g}=MN_1,\quad
 D_{\mathrm g}=MN_2.
 \tag{30}
\]
Their product is one, since the four displayed scalar powers multiply to one. Each trace is \(M+M^{-1}\): its eigenvalue ratio is prescribed by the native corner derivative, its determinant is one, and its trace tends to \(2\) at completeness. Thus the sign is fixed by continuity, rather than reset on a puncture independently.

The two disk words now agree with their actual geometric words, including their determinant-one lifts:
\[
 A_{\mathrm g}B_{\mathrm g}=M^{-2}W_2^{-1}W_0,\qquad
 (B_{\mathrm g}C_{\mathrm g})^{-1}
                         =M^{-2}W_1^{-1}W_3.
 \tag{31}
\]
These are the native \(v,w\) longitudes. Their selected eigenvalues are \(-Q,-P\), with their actual apex flags. The inverse in the second abstract word is essential to (31).

### 7.1. Actual auxiliary transports and character normalization

The native shaded paths send the corners as follows:
\[
 S_v:\infty\mapsto0,\quad 1\mapsto R;\qquad
 S_w:R\mapsto0,\quad 1\mapsto\infty.
 \tag{32}
\]
Their six white/shaded return identities imply, for the native punctures, that these paths reverse the oriented small boundary meridian at each endpoint. Thus
\[
 \begin{aligned}
 S_vC_{\mathrm g}S_v^{-1}&=B_{\mathrm g}^{-1},
 &S_vD_{\mathrm g}S_v^{-1}&=A_{\mathrm g}^{-1},\\
 S_wA_{\mathrm g}S_w^{-1}&=B_{\mathrm g}^{-1},
 &S_wD_{\mathrm g}S_w^{-1}&=C_{\mathrm g}^{-1}.
 \end{aligned}
 \tag{33}
\]
For example, the projective relation \(W_3S_v\sim S_v^-W_1\), together with
\(W_0S_v\sim S_v^-W_0\), gives
\[
 S_v(W_0^{-1}W_1)S_v^{-1}\sim W_0^{-1}W_3=N_0^{-1}.
\]
The native matrix representatives can differ by a nonconstant scalar in this calculation; those scalars are not set to one. Normalize the punctures using (30). The two sides now have determinant one and trace \(m\), so their projective equality has scalar \(+1\), since \(m\ne0\) near completeness. The remaining three identities follow from the other returns in the same way. This proves the literal determinant-one identities (33) without discarding a projective scalar.

Consequently
\[
                       V_{\mathrm g}=S_v^{-1},\qquad
                       T_{\mathrm g}=S_w^{-1}
 \tag{34}
\]
satisfy exactly (17). These are the actual positively marked auxiliary meridians of the native construction, not extra operators inserted into the tangle.

There is a regular marked conjugacy to the character coordinates. At completeness the selected \(M\)-eigenlines of \(A_{\mathrm g},B_{\mathrm g}\) are distinct. Their eigenlines vary holomorphically: the matrices minus their specified eigenvalue have rank one with a nonzero entry near the parabolic point. Send those two eigenlines to infinity and zero, then fix the residual diagonal conjugation by setting the upper-right entry of \(A\) to one. This entry is a unit near completeness. The pair becomes exactly (6), since \(\operatorname{tr}(AB)=-\beta\) fixes \(b=-\beta-2\).

The remaining matrix \(C\) is then determined by its trace, the two mixed traces, and \(\operatorname{tr}(ABC)=m\), giving (7). The common centralizer of this irreducible pair consists only of scalars. Hence a transport satisfying (17) is unique projectively: the ratio of two such transports commutes with both punctures. Its marked eigenvalue ratio is therefore (20), not a new free parameter.

The branch is fixed by the literal complete matrices. Substituting the complete native white maps gives
\(A_{\mathrm g}=\left(\begin{smallmatrix}3-2i&-1+i\\4-4i&-1+2i\end{smallmatrix}\right)\)
and
\(C_{\mathrm g}=\left(\begin{smallmatrix}1&-1+i\\0&1\end{smallmatrix}\right)\).
Their product has trace \(2+8i\). Since \(S=8\), the character coordinate \((\operatorname{tr}(A_{\mathrm g}C_{\mathrm g})-2)/S\) is \(i\), not the inverse root.

Let \(X_{\mathrm g}\) denote the native source wire extracted from its actual auxiliary meridian:
\[
 U_v^{\exp}=\frac{Q+X_{\mathrm g}}{1+QX_{\mathrm g}}.
 \tag{35}
\]
The character coordinate \(E\) has the same ratio by (20). For \(Q^2\ne1\), the fractional-linear map in (35) is injective, so \(E=X_{\mathrm g}\). Holomorphic continuation establishes equality through \(Q=1\). Equivalently,
\[
 \operatorname{tr}(A_{\mathrm g}C_{\mathrm g})
       =2+\bigl[\beta+\gamma+(M+M^{-1})^2\bigr]X_{\mathrm g}.
 \tag{36}
\]
This proves the matching branch, rather than choosing the inverse root because the two have the same discriminant.

### 7.2. Main basepoint, selected flag, and negative lift

The native geometric longitude based at infinity is
\[
 \Lambda_\infty=S_wS_v^{-1}S_w^{-1}S_v.
 \tag{37}
\]
Its positively oriented main meridian is \(C_{\mathrm g}=MN_1\). In the native chart it is exactly
\[
 C_{\mathrm g}=
 \begin{pmatrix}
 M^{-1}&M E_0-M^{-1}\\0&M
 \end{pmatrix},
 \tag{38}
\]
where \(E_0\) is the native white-face coordinate. Thus infinity is its actual \(M^{-1}\) source flag. The white-face coordinate \(E_0\) need not equal the source coordinate \(E=X_{\mathrm g}\) away from \(M=1\).

Our abstract commutator is based at the corner \(R\), whose positive meridian is \(A_{\mathrm g}\). The actual path
\[
 U=S_w^{-1}S_v,\qquad
 \infty\longrightarrow 0\longrightarrow R.
 \tag{39}
\]
transports both the meridian and longitude:
\[
 UC_{\mathrm g}U^{-1}=A_{\mathrm g},\qquad
 U\Lambda_\infty U^{-1}
      =S_w^{-1}S_vS_wS_v^{-1}
      =T_{\mathrm g}V_{\mathrm g}^{-1}
                         T_{\mathrm g}^{-1}V_{\mathrm g}.
 \tag{40}
\]
The first identity follows from (33), including its two inversions; the second is literal multiplication of the four words. The source \(M^{-1}\) eigenflag is transported by this same path. It is not identified with infinity in the normalized matrix (6), where infinity is instead the \(M\) eigenline.

Equations (25), (36), and (40) identify the native longitude eigenvalues exactly: on its source \(M^{-1}\) eigenflag the value is \(-u^{-1}\); on the preferred \(M\) flag it is \(-u\). The negative sign survives the basepoint change. At completeness the native matrix is
\[
 \Lambda_\infty=
 \begin{pmatrix}-1&2+2i\\0&-1\end{pmatrix},\qquad
 C_{\mathrm g}=
 \begin{pmatrix}1&i-1\\0&1\end{pmatrix}.
 \tag{41}
\]
Their projective translations have ratio \(2i\), equal to (27). This checks the actual marked complete lift and scale; it is not the reason for the full rational identification above.

Thus the two independent constructions agree on the canonical pure block, its main eigenvalue, its two primitive auxiliary words, and its negative main-longitude lift. Arbitrary ordered-tree concatenation, preferred global framing, and the native odd or parallel-strand changes remain the separate assembly questions.

## 8. Odd collars: an exact fixed-chart obstruction and the required flag transport

### 8.1. The old vertex swap fails if the white maps are held fixed

There is a short one-parameter test entirely within the native pure gluing locus. Set the two auxiliary parameters \(Q=P=1\) and use
\[
 E_0=\frac{i}{M},\qquad
 R=\frac1{1+M^2},\quad S=\frac{M^2}{1+M^2},\quad
 A_v=\frac{i}{M+i},\quad a_v=\frac{M}{M+i}.
 \tag{42}
\]
Here \(A_v,a_v\) are geometric apex coordinates, not the puncture matrix \(A\). Substitution in the native polynomial \(G\) gives zero: at \(Q=P=1\), that polynomial is
\(4(m+1)(mE_0^2+1)\), with \(m=M^2\).

Keep all four native white maps of the pure chart. Let \(A_o,B_o\) be the unique Möbius maps with the old odd vertex permutations
\[
 A_o:(A_v,\infty,1)\mapsto(a_v,S,0),\qquad
 B_o:(A_v,R,0)\mapsto(a_v,\infty,1).
 \tag{43}
\]
They have explicit representatives
\[
 A_o=\begin{pmatrix}S&-S\\1&S(A_v-1)/a_v-A_v\end{pmatrix},
 \qquad
 B_o=\begin{pmatrix}
 [a_v(A_v-R)+R]/A_v&-R\\1&-R
 \end{pmatrix}.
 \tag{44}
\]
Direct substitution of (42) and the native white matrices gives
\[
 W_0^{-1}B_oW_2^{-1}A_o
 \ \sim\
 \begin{pmatrix}
 M^{-4}&i(M^2-1)(M-i)/M^4\\0&1
 \end{pmatrix}.
 \tag{45}
\]
This is not the identity for general \(M\) arbitrarily close to one. In contrast, the third old return
\(W_1^{-1}B_oW_3^{-1}A_o\) is projectively the identity on this family. Thus agreement at completeness, or checking only that third return, would miss the failure.

Equation (45) is an obstruction to keeping the pure white charts while applying the old three-point permutations. It does not obstruct the actual braid mapping cylinder, whose neighboring charts and marked eigenflags must be transported with the braid.

### 8.2. The regular matrix implementing the actual Hurwitz move

Let \(A,B\in\mathrm{SL}_2\) have the same trace, and put \(P=BA\). The actual positive collar convention in the marked source is
\[
 (A,B)\longmapsto(A^{-1}BA,A),\qquad
 K=P^{-1}-I.
 \tag{46}
\]
The matrix \(K\) implements this conjugation. One way to prove it is first to set \(C=AB\), \(H=C-I\). Equal traces and the two Cayley--Hamilton identities give
\[
 HB=AH,\qquad
 H^2=(\operatorname{tr}C-2)C,\qquad
 \det H=2-\operatorname{tr}C.
 \tag{47}
\]
Thus \(H\) implements the Hurwitz move preserving \(AB\),
\((A,B)\mapsto(ABA^{-1},A)\). Changing to the ordered product \(BA\) gives (46); \(P^{-1}-I\) is projectively \((P-I)^{-1}\).

At auxiliary eigenvalues \(-Q,-Q^{-1}\), these matrices are regular near completeness: their determinant is near four. The selected eigenvalue ratio of \(H\) is \(Q\), whereas the selected ratio of \(K=P^{-1}-I\) is \(Q^{-1}\). This distinction matches the actual ordered collar; calling \(H\) the positive crossing without changing its ordered product would reverse the sign.

### 8.3. Equal and opposite decorated eigenvalues behave differently

Suppose first that \(Aa=\lambda a\) and \(Bb=\lambda b\), with independent nonzero vectors \(a,b\). In their ordered basis,
\[
 A=\begin{pmatrix}\lambda&\alpha\\0&\lambda^{-1}\end{pmatrix},
 \quad
 B=\begin{pmatrix}\lambda^{-1}&0\\\beta&\lambda\end{pmatrix},
 \quad
 K=\begin{pmatrix}\alpha\beta&-\alpha/\lambda\\-\beta\lambda&0\end{pmatrix},
 \quad\det K=-\alpha\beta.
 \tag{48}
\]
Consequently
\[
 \frac{(Ka)\otimes(Kb)}{\det K}
       =-\lambda^{-1}(A^{-1}b)\otimes a.
 \tag{49}
\]
Likewise \(((Ha)\otimes(Hb))/\det H=-\lambda(Ab)\otimes a\) for the \(AB\) convention. These are exact vector-tensor identities. At \(\lambda=M^{-1}\), the raw factor in (49) is \(-M\); its reciprocal is \(-M^{-1}\). A use in a dual or inverse comparison must specify which of those factors it requires.

The equal-eigenvalue hypothesis cannot be removed. If instead
\(Aa=\lambda a\) and \(Bb=\lambda^{-1}b\), then
\[
 A=\begin{pmatrix}\lambda&\alpha\\0&\lambda^{-1}\end{pmatrix},
 \quad
 B=\begin{pmatrix}\lambda&0\\\beta&\lambda^{-1}\end{pmatrix},
 \quad
 K=\begin{pmatrix}
 \alpha\beta+\lambda^{-2}-1&-\alpha\lambda\\
 -\beta\lambda&\lambda^2-1
 \end{pmatrix}.
 \tag{50}
\]
In particular \(Kb=(-\alpha\lambda,\lambda^2-1)^{\mathsf t}\), which is not on the line of \(a\) for \(\lambda^2\ne1\).

For the native pair \(A_{\mathrm g},B_{\mathrm g}\), the actual ideal corner flags at \(R,0\) have eigenvalues \(M^{-1},M\), respectively. This follows from their native derivatives \(M^2,M^{-2}\). Thus (50), not automatically (48), describes those two decorated ideal vertices.

The natural decorated version of (46) is
\[
 (A,B;\ell_A,\ell_B)
 \longmapsto
 (A^{-1}BA,A;\ A^{-1}\ell_B,\ell_A).
 \tag{51}
\]
If the selected eigenvalues agree, \(K\) carries the two old lines to the two lines displayed in (51). If they are opposite, it carries the opposite eigenline of each input puncture to the displayed output line. Indeed \(KAK^{-1}=A^{-1}BA\) and \(KBK^{-1}=A\), so the eigenvalue of each transported line is unchanged; the desired output line instead carries the other input's selected eigenvalue.

This gives a precise prescription for a decorated collar: use the actual Hurwitz representation and develop the output triangles from the naturally transported flags in (51). When the two selected eigenvalues differ, this cannot be replaced by applying \(K\) to the two old ideal vertices and keeping the neighboring white charts unchanged. On the marked eigenvalue cover the alternative eigenlines vary holomorphically and coalesce at \(M=1\), which is why the distinction disappears at the complete point.

To finish an arbitrary oriented-tree theorem, the physical endpoint types must specify which eigenflags occur on each side of the braid mapping cylinder, and the adjacent white maps must be recomputed from those output flags. The unframed Hurwitz identity alone does not establish that final decorated sewing or its global preferred-longitude factor.
