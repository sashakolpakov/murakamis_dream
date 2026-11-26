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
