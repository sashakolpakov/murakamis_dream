# Two actual octahedra in angular longitude coordinates

1 November 2026. Private derivation. The local charts and positivity
below concern the actual two-leaf Conway cut. A general ordered
edge-block decomposition is stated separately as the remaining global
topological obligation; no new short-filling volume theorem is asserted.

## 1. The actual two-leaf model

Start with the literal two-leaf closure \(C(h_0T(h_1))\). At a
pure leaf use the original coordinates
\[
 Q=(0,\infty,1,R),\qquad
 Z=\frac{1+E}{1+H},\qquad
 E=e^{2\pi ix},\quad H=e^{2\pi it},
 \quad R=\frac{H(1+E)^2}{E(1+H)^2}.
\tag{1}
\]
The second projection copy has apex \(Z/E\), not a conjugation of
the free parameters. The original turn and root closing maps are
\[
 T(z)=\frac{R_1-1}{z-1},\qquad
 C(z)=\frac{z-R}{z-1},\qquad R_1=1-R.
\tag{2}
\]
These are the actual maps of
`notes/actual_conway_general_mask_marked_filling.md`, equations
(11), (14), and the original closed projection cut. In particular
both maps must be used when placing the second leaf. Applying only
the turn would put the two complete apices at the same point.

The complete two-leaf wire is \(x=1/4\). In each projection ball,
the two ideal pyramids are joined along their ordered quadrilateral
bases. Their six outer vertices form an octahedron. This is a
literal local cut statement, not a deduction from its volume.

## 2. Solving in the two angular longitude variables

Write \(\tau_0=\tau\), \(\tau_1=\upsilon\), and prescribe
the actual disk longitude logarithms
\[
                          V_j=2i\tau_j.
\tag{3}
\]
The pure leaf relation gives \(v_j=-i\tau_j\), where
\(v_j=\log[\sin\pi(x-t_j)/\sin\pi(x+t_j)]\).
On the branch through completeness, put
\[
 y=\tan(\tau/2),\qquad z=\tan(\upsilon/2),\qquad
 k=(1+y^2+z^2)^{-1/2},\qquad k(0,0)=1.
\tag{4}
\]
Then the exact solution of the two-leaf stationarity equations is
\[
\begin{aligned}
 \tan(\pi x)&=k,\\
 \tan(\pi t_0)&=iky,&
 \tan(\pi t_1)&=ikz,\\
 E&=\frac{1+ik}{1-ik},&
 H_0&=\frac{1-ky}{1+ky},&
 H_1&=\frac{1-kz}{1+kz},\\
 R&=\frac{1+z^2}{2+y^2+z^2},& R_1&=1-R,\\
 Z_j&=\frac{1+E}{1+H_j}.
\end{aligned}
\tag{5}
\]
Indeed the logarithmic ratio equation first gives
\(\tan\pi t_j=ik\tan(\tau_j/2)\). Its ordered metric is
\[
 \kappa_j=\frac{k^2(1+\tan^2(\tau_j/2))}
                       {1-k^2\tan^2(\tau_j/2)}.
\tag{6}
\]
The wire equation is \(\kappa_0\kappa_1=1\). With
\(a=y^2+z^2\), it factors as
\((k^2+1)((1+a)k^2-1)=0\); the complete branch is (4).
Thus \(\kappa_0=(1+y^2)/(1+z^2)\), which yields (5).
No meridian-color approximation was used.

The two octahedra have the same equator
\(q=(0,\infty,1,R)\), and apices
\[
\begin{array}{c|cc}
 & A & B\\ \hline
 +&Z_0&\displaystyle\frac{RZ_1}{Z_1-R_1}\\[2mm]
 -&Z_0/E&\displaystyle\frac{RZ_1}{Z_1-ER_1}.
\end{array}
\tag{7}
\]
For example, composing (2) gives
\(C(T(Z_1))=RZ_1/(Z_1-R_1)\). Replacing the second-copy apex by
\(Z_1/E\) gives the last entry. At zero the two rows are
\[
 (A_+,B_+)=((1+i)/2,(1-i)/2),\qquad
 (A_-,B_-)=((1-i)/2,(1+i)/2).
\tag{8}
\]
The corresponding complete cells are the regular octahedra in their
opposite labeled orientations.

## 3. Uniform positive tetrahedra on an explicit complex bidisk

Subdivide the plus octahedron into the four tetrahedra with ordered
vertices \((A_+,B_+,q_j,q_{j+1})\), \(j\bmod4\). Reverse the
last two vertices in the minus copy. Use the cross ratio
\[
 [a,b,c,d]=\frac{(a-c)(b-d)}{(a-d)(b-c)}.
\tag{9}
\]
All eight complete shapes are \(i\). This triangulates the actual
two-pyramid union, with the internal diagonal joining its two apices.

There is a uniform positive chart on
\[
                    |\tau|,|\upsilon|\le 10^{-2}.
\tag{10}
\]
Here are deliberately loose explicit bounds. The elementary sine and
cosine series give \(|y|,|z|<0.005001\). Hence
\(|y^2+z^2|<0.000051\), \(|k-1|<0.000026\),
\(|E-i|<0.00006\), \(|H_j-1|<0.0102\), and
\(|R-1/2|<0.000026\). Substitution in (5) gives
\(|Z_j-(1+i)/2|<0.004\). In each denominator in the B column
of (7), the complete modulus is \(1/2\), and its perturbation
is less than \(0.0041\). The quotient estimate therefore bounds
the motion of each finite vertex in (7) by \(0.02\); the
remaining finite equatorial vertices are fixed or move by less than
\(0.000026\).

Every finite pair of distinct complete vertices occurring in (9)
has separation at least \(1/2\). Each difference factor therefore
changes by relative size less than \(0.08\). Comparing both the
numerator and denominator products with one bounds the cross-ratio
quotient change by
\[
             \frac{4(0.08)+2(0.08)^2}{(1-0.08)^2}<0.4.
\tag{11}
\]
For a factor involving infinity there are fewer factors and the same
bound suffices. Thus every ordered shape lies in \(|w-i|<0.4\),
and in particular has positive imaginary part. All denominators and
ideal vertices remain distinct. The internal diagonal has total
angle \(2\pi\): its product relation telescopes exactly, and its
integer angle branch is fixed by (8).

This is positivity of the actual local geometric tetrahedra, not
positivity of the original real \((x,t_j)\) angle chamber. For
complex angular parameters the equatorial quadrilateral need not
be planar. The triangular octahedral boundary and the positive
tetrahedral subdivision are the retained geometric objects.

## 4. The two disk-side pants depend only on their longitude

The local white matrices in a leaf frame are
\[
\begin{aligned}
 W_0&=\begin{pmatrix}1&0\\0&E\end{pmatrix},&
 W_1&=\begin{pmatrix}1&E-1\\0&E\end{pmatrix},\\
 W_2&=\begin{pmatrix}E-R&R(1-E)\\E-1&1-ER\end{pmatrix},&
 W_3&=\begin{pmatrix}R&0\\1-E&ER\end{pmatrix}.
\end{aligned}
\tag{12}
\]
The relation \(Z^2-(1+E)Z+ER=0\) is retained. Put
\[
                Q=\frac{E-Z}{Z-1}=e^{-v}=e^{i\tau}.
\tag{13}
\]
The incoming shaded triangle has cyclic vertices \((Z,\infty,1)\),
and the outgoing one has \((Z,R,0)\). A disk cut doubles each
of them across its adjacent white faces, producing the actual
two-triangle pants boundary. In the plus chart, transport the
opposite triangle through the appropriate \(W_j^{-1}\).

If an oriented edge has endpoints \((a,b)\) and the third
vertices on its two sides are \(c,d\), measure its complex
ratio by (9). Direct substitution gives the following cyclic tables:
\[
\begin{array}{c|ccc}
\text{incoming edge}&(Z,\infty)&(\infty,1)&(1,Z)\\ \hline
\text{ratio}&-Q^{-1}&-Q&-Q^{-1}\\[1mm]
\text{outgoing edge}&(Z,R)&(R,0)&(0,Z)\\ \hline
\text{ratio}&-Q&-Q^{-1}&-Q.
\end{array}
\tag{14}
\]
For example the first incoming ratio is
\((1-Z)/(E-Z)=-Q^{-1}\). Across its base edge, the opposite
apex is \(W_1^{-1}(Z/E)=Z-E+1\), giving \(-Q\).
For the outgoing base, its opposite apex is
\(W_3^{-1}(Z/E)=ER/(2E-Z)\), giving \(-Q^{-1}\).
The remaining entries follow in the same way from (12).

This table removes the other endpoint's angular parameter completely.
It also retains the shear, not just the plane angle. The two main
puncture products are one; the third puncture product is
\(Q^{\pm2}\), with the actual disk longitude having multiplier
\(Q^2=e^{2i\tau}\). The sign of the oriented pants boundary is
the inverse convention already recorded by the original marked
disk word.

Consequently an outgoing disk-side boundary of one local block and
an incoming boundary of another with the same \(\tau\) have
inverse edge ratios under the original puncture matching. Normalize
one triangle by its three ordered vertices. The other triangle's
position is then fixed by (14), so the whole two-triangle transition
matches. Their edge shears cancel and their interior-angle branches,
continued from \(\pi\), sum to \(2\pi\). This is the local
geometric seam calculation required for joining edge blocks. It does
not assert an arbitrary reordering of the three punctures.

## 5. Local logarithmic increments and the edge action

Let \(\psi(\tau,\upsilon)\) be the pure two-leaf action in
the angular variables, retaining its complete constant. Its actual
Legendre relation gives
\[
 \partial_\tau\psi=it_0
   =-\frac1\pi\operatorname{arsinh}
                   (\tan(\tau/2)\cos(\upsilon/2)),
\tag{15}
\]
with the branch through zero; interchange the endpoints for the other
derivative. To verify the last equality, use
\(\operatorname{artanh}(ky)=
\operatorname{arsinh}(y/\sqrt{1+z^2})\).

The local pure meridional increment is therefore
\[
                -2\pi it_0=-2\pi\partial_\tau\psi.
\tag{16}
\]
It is a small actual log-link increment in this fixed local chart.
If a genuine disk-page assembly concatenates these local paths in
their original order, its total pure meridian period is the sum of
(16). A single retained half twist of sign \(\epsilon_v\)
adds \(-\epsilon_vV_v/2\), in the already proved primitive basis.
It would then give
\[
 U_v=-2\pi\sum_{e\sim v}\partial_{\tau_v}\psi_e
                         -i\epsilon_v\tau_v,
 \qquad V_v=2i\tau_v.
\tag{17}
\]
The direct first-charge saddle with \(n_v=\epsilon_v-2p_v\)
would make (17) exactly \(U_v+p_vV_v=-2\pi i\).
The integer would be obtained by concatenating actual small local
increments, even when the total is no longer a small logarithm.

## 6. Precise status of the global construction

The local model suggests a concrete finite assembly. Associate the
two octahedra above to each physical edge of a circle-only tree.
At a circle vertex, list its incident edges in the actual cyclic
order and join the corresponding outgoing and incoming disk-side
pants cyclically. Insert the prescribed retained half twist at its
specified disk page. Table (14) supplies geometric seam matching
for a common angular variable at that circle. The complete model
has two octahedra per edge and the expected cusp lattice with
\(D\) meridional sectors at a degree-\(D\) circle.

What still requires a full topological proof is that this assembly
is the literal original augmented Conway exterior with its primitive
disk paths, for every stated ordered tree. The existing belt-stack
cut proves the corresponding cyclic insertion at one outer disk.
The general rigid-spine theorem proves the volume and actual marked
geometry by different cells, and explicitly does not provide this
octahedral decomposition. Equality of their source actions or complete
volumes cannot supply the missing identification.

A proposed proof should cut the original circle neighborhood into
ordered disk pages, one between each adjacent product factor, and
show by terminal-vertex removal that each physical quarter-turn
isolates precisely the two-leaf block with its four marked main
segments. The two-circle endpoint pairs are interlaced; that is the
actual quarter-turn, not a commutative source substitution. It must
also show that the primitive meridian crosses these pages once in
their cyclic order, with only the recorded half-twist shear. This
would justify the hypothesis used in (17).

Once that identification is supplied, (10), (14), and the actual
period equation give the finite positive-cell/log-link certificate
of `md-short-filling-geometric-certificate-and-real-chamber-obstruction.md`.
The current analytic condition makes every angular parameter much
smaller than the explicit radius (10). No geometric conclusion for
that whole class is claimed here before the ordered disk-page and
primitive-path identification is proved.
