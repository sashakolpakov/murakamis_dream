# Full-Psi ray patterns on the actual crossing boundary

Private written proof, 17 November 2026. The entire negative-ray
functional of the original scalar cycle has a finite, explicit
replacement at each original crossing. We compute both signed
replacement matrices and their literal nine-cell boundary arrays.
This transports a supplied original exterior observation; it does
not replace that observation by a fixed-zero cut or by scalarity.
The single finite reciprocal wall of [W] is not substituted for a ray.

## 1. The original ray moments and their finite support

Put \(N>2\) odd, \(d=N-1\), \(Q=e^{2\pi i/N}\),
\(x=-e^{-\pi i/N}\), and \(p_a=(Q;Q)_a\).
All residues in square brackets lie in \(0,\ldots,d\).
The complete point has \(|x|=1\), \(x^N=1\).
The finite moments in [F] are
\[
 v_{+,a}=\frac{(-1)^aQ^{a(a-1)/2}}{p_a},\qquad
 v_{-,a}=\frac{Q^a}{p_a}.
 \tag{1}
\]
Keep the indicated logarithmic lip in the full function
\(\Psi_\epsilon\), and define its signed ray coefficient by
\[
 j_{\epsilon,a}(R)=
 -\frac{\epsilon(-1)^{N-a}}{2\pi i}
 \int_0^R\Psi_\epsilon(\log r+i\epsilon\pi)
                       r^{N-a-1}\,dr,\qquad 0\le a<N.
 \tag{2}
\]
The circle coefficient is \(v_{\epsilon,a}-j_{\epsilon,a}(R)\).
Thus the circle plus (2), including its sign, is exactly (1).
From [F,(5)],
\[
 |j_{\epsilon,a}(1)|
 \le \frac{\sqrt2}{2\pi(N-a)}.                       \tag{3}
\]
No value at \(a=N\) is used.

For an atom chosen as original, circle, or ray, write
\(b_{\epsilon,a}\) for respectively \(v_{\epsilon,a}\),
\(v_{\epsilon,a}-j_{\epsilon,a}\), or \(j_{\epsilon,a}\).
The exact coefficient replacements in the ordered source are
\[
\begin{array}{c|c}
\text{atom}&\text{coefficient of order or head index }a\\ \hline
U_\pm&x^{-a}Q^{-a}b_{-,a}\\
V_\pm&x^{-a}b_{+,a}\\
F^{-1}&Q^{-a}b_{-,a}\\
F&NQ^{d-a}b_{+,d-a}.
\end{array}                                                   \tag{4}
\]
In particular the reflected factorial uses the complementary
moment index, its full \(N\), and its original \(Q\)-shift.
One does not replace a factorial coefficient by \(j_{\epsilon,a}\)
without these factors.

The support assertion used here is the coefficient-independent
one in [F, Sections 3 and 8]. It is true for arbitrary numerical
atom coefficients and real nonnegative flows: every moment order
is in \([0,d]\), both before and after the head-forest contraction.
Consequently (4) applies to every circle/ray pattern of the
original whole source. It is not an expansion on an independently
chosen fixed head torus.

## 2. Every entry of the signed modified crossing

Use the strict checked crossings of [E,(1)], with their common
Cartan factors \(\kappa^{\pm1}\) retained externally:
\[
 M_+^0=C D U_+C^{-1},\quad M_-^0=C V_+D^{-1}C^{-1},
\quad
 C=F_2U_-F_1F_2^{-1},\quad
 C^{-1}=F_2F_1^{-1}V_-F_2^{-1}.                     \tag{5}
\]
Here
\[
 D|a,b\rangle=d_b|a,b\rangle,\qquad
 d_b=(-1)^bQ^{b(b-1)/2}x^{-2b}.
\]
Its Gaussian realization in [F] is integrated with the original
Gaussian measure; it gives this same diagonal for every coefficient
replacement. At the complete point all \(d_b\) have modulus one.

Number the nine moment atoms from right to left:
\[
\begin{array}{c|ccccccccc}
\text{number}&1&2&3&4&5&6&7&8&9\\ \hline
\text{atom}&F_2^{-1}&V_-&F_1^{-1}&F_2&
 U_+\ (\!+\!),\,V_+\ (\!-\!)&
 F_2^{-1}&F_1&U_-&F_2 .
\end{array}                                                   \tag{6}
\]
Each may have its own choice in (4). Denote its resulting coefficient
by \(h_j\). In a positive crossing \(D\) occurs after atom 5 and
before atom 6; in a negative crossing \(D^{-1}\) occurs after
atom 4 and before atom 5.

For input \((a,b)\), output \((u,v)\), and transfer orders \(r,t,s\),
put
\[
 A=a-r+t,\quad B=b+r-t,\quad s=A-u,\qquad
 g_+(r,t)=d_B,\quad g_-(r,t)=d_{b+r}^{-1}.
 \tag{7}
\]
Then the replacement matrix is exactly
\[
\boxed{\begin{split}
 M^\sigma_{uv;ab}
 ={}&\delta_{u+v,a+b}\,h_9(v)h_1(b)\\
 &\times\sum_{r,t}
 h_2(r)h_3(a-r)h_4(b+r)h_5(t)\,
 g_\sigma(r,t)h_6(B)h_7(A)h_8(A-u).
\end{split}}                                                   \tag{8}
\]
The ranges are the ordinary integer inequalities
\[
\begin{split}
0&\le r\le\min(a,d-b),\\
0&\le t\le\min(b+r,d-a+r),\\
0&\le A-u\le\min(A,d-B).
\end{split}                                                     \tag{9}
\]
All external indices lie in \(0,\ldots,d\). The delta in (8) is
ordinary integer equality, not merely a congruence.

To prove (8), atom 2 sends \((a,b)\) to \((a-r,b+r)\);
atom 5 sends that pair to \((A,B)\); atom 8 sends it to
\((A-s,B+s)\). The six diagonal factors have the six arguments
shown in (8). Truncation of these three transfers gives (9).
This proves the formula before any cancellation of coefficients.
For the original choices it is (5); for any ray pattern it is its
actual full-Psi moment replacement, including all endpoint orders.

An immediate coefficient norm bound follows without analyzing
cancellation. Each diagonal contributes its coefficient supremum,
and each transfer contributes its coefficient \(\ell^1\) norm.
The stronger uniform full-ray theorem [A] retains the \(a=d\)
endpoint and proves \(c/N\le |j_{\epsilon,a}|\le C/N\), for every
physical \(a\) and all sufficiently large \(N\).
A ray transfer therefore has norm at most \(C\), a reciprocal
factorial ray at most \(C/N\), and a reflected factorial ray at
most \(C\). The transfer inverse has norm at most
\(CN e^{C\sqrt N}\); the two diagonal inverse bounds are \(CN\)
and \(C\). The unit multiples of the truncated shifts in (4)
satisfy exactly the hypotheses \(\|T\|\le1,T^N=0\) of [A].
Choosing rays at all nine atoms consequently gives the actual
invertible crossing reference
\[
 \boxed{\|M^\sigma_{\rm ray}\|_2\le C N^{-3},\qquad
 \|(M^\sigma_{\rm ray})^{-1}\|_2
                       \le C N^6e^{C\sqrt N}.}                 \tag{10}
\]
There are three factors of each type; multiplying them in the
literal order (5) proves (10). This uses no lower bound for an
observed matrix element. For a mixed pattern the product of its
actual nine coefficient bounds remains valid; (10) is not
asserted for every nonempty ray pattern.

## 3. Both literal Fourier adapters

Let \(F_{ia}=N^{-1/2}Q^{ia}\), \(\mathcal F=F\otimes F\),
\(D_x|a\rangle=x^a|a\rangle\), and let \(P\) flip two heads.
The actual bridge proved in [W,(15)] is
\[
 R^o_M=Q\mathcal F(D_x^{-1}\otimes I)P M
                 (I\otimes D_x)\mathcal F^{-1}.                \tag{11}
\]
This defines the positive planar replacement for every matrix \(M\);
for \(M=M_+^0\) it is the original unbraided crossing.
The canonical planar array is
\[
             R^+_M(i,j,k,l)=Q^{-k-l}(R^o_M)_{ij;kl}.
 \tag{12}
\]
Every displayed adapter in (11) is unitary. In particular no
factorial similarity has been suppressed.

The negative convention must be derived separately. Put
\[
             U=\mathcal F^{-1}(D_x\otimes I)P .
 \tag{13}
\]
Transposing (11) and using the actual braid convention
\(B_{K,+}=P(R^o)^t\) gives
\[
 B_{K,+}=Q U(M_+^0)^tU^{-1},\qquad
 B_{K,-}=Q^{-1}U(M_-^0)^tU^{-1}.                    \tag{14}
\]
The second equation follows by inversion of the first.
By [Q, Section 1] the printed negative planar crossing has an
additional factor \(Q\), and its cyclic labels are
\((i,j,k,l)=(\text{input}_2,\text{output}_2,
\text{output}_1,\text{input}_1)\).
Therefore its raw south-sector replacement is
\[
             R^-_M(i,j,k,l)
                 =Q^{-j-k}(UM^tU^{-1})_{k,j;l,i}.     \tag{15}
\]
Its sector is \((0,0,0,1)\). Equations (14),(15) retain the
inverse-crossing phase rather than assuming the printed negative
matrix is the inverse.

## 4. A single finite entry on the nine-cell boundary

Use the actual paired-face coordinates and their two lips:
\[
 k_m=\alpha_{m,-}-\alpha_{m,+}+h_m,\qquad
 f_m(k)=s_{0m}^{[k-1]}s_{m5}^{[-k]},\qquad
 \mathcal A_m(\alpha;i)=f_m(k_m)Q^{ik_m}.
 \tag{16}
\]
Keep the scalar \(C_N(\mathbf s)\) of [C,(4)] unchanged.
Write \(\phi_+=3(h_1-1)/2\).
For sector \((0,0,0,1)\), [Q,(10)] gives
\(d_\chi=1/2-3h_1/2\), so the full exponent in [C,(38)] is
\(\phi_-=3(h_1-1)/2+d_\chi+1=0\).
This is its retained normalization, not a newly chosen
negative-crossing scalar.

For a positive replacement set
\[
 u=[-k_1],\quad v=[-k_2],\quad
 a=[k_3-1],\quad b=[k_4-1].
\]
The complete eight-face replacement array is
\[
\boxed{\mathcal E_+(M)_\alpha
 =C_NQ^{\phi_+}s_{05}^d\,N^2Qx^{b-u}
       \prod_{m=1}^4f_m(k_m)\,M_{v,u;a,b}.}           \tag{17}
\]
For a negative replacement set
\[
 \gamma=[-k_1],\quad\delta=[-k_4],\quad
 \alpha_0=[k_2-1],\quad\beta=[k_3-1].
\]
Then
\[
\boxed{\mathcal E_-(M)_\alpha
 =C_NQ^{\phi_-}s_{05}^d\,N^2x^{\beta-\delta}
       \prod_{m=1}^4f_m(k_m)\,
             M_{\gamma,\delta;\alpha_0,\beta}.}       \tag{18}
\]
In (17),(18), substitute the explicit sum (8) for the matrix entry.
This describes every boundary coefficient and its exact support.
For example the positive support satisfies
\([{-k_1}]+[{-k_2}]=[k_3-1]+[k_4-1]\), as ordinary integers.
It implies \(\sum_mk_m=2\) modulo \(N\), but the integer equality
and the path inequalities (9) are stronger.

Here is the direct Fourier proof, including its normalizations.
Substitute (11),(12) in
\[
 C_NQ^{\phi_+}s_{05}^d
       \sum_{i,j,k,l}R^+_M(i,j,k,l)
                  \prod_m f_m(k_m)Q^{i_mk_m}.
 \tag{19}
\]
The four finite sums force the four residues in (17).
They contribute \(N^4\); the two two-head Fourier factors contribute
\(N^{-2}\). The remaining diagonal is \(Qx^{b-u}\).
For (15), expand
\[
 (UM^tU^{-1})_{k,j;l,i}
 =N^{-2}\sum_{h,g,h',g'}
    Q^{-kg-jh+g'l+h'i}x^{g-g'}M_{h',g';h,g}.
\]
The four sums now force
\((h',g',h,g)=(\gamma,\delta,\alpha_0,\beta)\);
their remaining factor is precisely that in (18).
This proves both identities without an inverse-crossing estimate.
For the original matrix (19) is the literal nine-cell array by [C].
For a replacement it defines its specified all-boundary insertion
through the same proved invertible port maps.

No cyclic seam has been smoothed. In particular
\[
 \frac{f_m(k+1)}{f_m(k)}
 =\frac{s_{0m}}{s_{m5}}
 \left[1+\left(\frac{s_{m5}^N}{s_{0m}^N}-1\right)
                           \delta_{k0}\right].       \tag{20}
\]
An arbitrary sector gauge is carried by the actual port translations
of [W,(28)], and the full scalar of [C,(38)].
It cannot be imposed on (17) without those same translations.

On fixed compact sets of injective real decorations, with real odd
roots, \(|C_N|=N^{-2}\), and all other absolute factors in (17),(18)
are bounded above and below independently of \(N\). Thus, for the
unnormalized Euclidean norm on all eight face indices,
\[
 c_KN^2\|M\|_{\rm HS}\le
       \|\mathcal E_\sigma(M)\|_2
       \le C_KN^2\|M\|_{\rm HS}.                    \tag{21}
\]
Indeed the residue-to-matrix-index map is a bijection, and each
four-residue choice has \(N^4\) face-pair lifts.
Since \(\|M\|_{\rm HS}\le N\|M\|_2\), (10) gives the explicit
all-ray array bound \(C_K\), for all sufficiently large levels.
The opposite singular-value bound in (10) also gives
\(\|\mathcal E_\sigma(M_{\rm ray})\|_2
\ge c_KN^{-3}e^{-C\sqrt N}\).
These are replacement-array bounds, not bounds for a quotient
by an exponentially small observed scalar.

## 5. The original relative functional and exterior row

For an unintegrated ray coordinate \(t>0\), use the density
\[
 \omega_\epsilon(t)=
 -\frac{\epsilon}{2\pi i}
       \Psi_\epsilon(\log t+i\epsilon\pi)(-t)^N\,\frac{dt}{t}
 \tag{22}
\]
and replace its moment coefficient in (4) by \((-t)^{-a}\).
For a circle use its original circle density and \(t^{-a}\).
The matrix (8) and arrays (17),(18) are then finite Laurent
polynomials of degree at most \(d\) in each inverse moment variable.
Their integrals against (22) give exactly the integrated formulas
(2),(4),(8). The Gaussian variables retain their original measure.

This exchange of contraction and integration is the actual one in
[F], not a new convergence assumption. Its continuous-flow bound
is \(\prod_{\rm rays}t^{-d}\) times a fixed polynomial in logarithms
and \(\exp(C_{\rm word}N(1+\sum|\xi|))\).
Since \(|\omega_\epsilon(t)|=\sqrt{1+t}\,t^{N-1}dt/(2\pi)\),
the inner ends are integrable, including the original coupled caps.
The Gaussian weight controls the displayed \(\xi\) factor.
Therefore all finite contractions above commute with the original
joint integral. Common radial cutoffs and the original lip/interval
gluing are retained when taking relative boundaries. No period is
assigned separately to a divergent component of an intersecting
wall decomposition.

The exterior is not changed to a favorable cut. For example, in the
literal averaged braid presentation of [E,(4)], a whole-word matrix
\(T\) has the specified observation
\[
 \nu_E(T)=\frac1N
 \sum_{p,q=0}^d\sum_{\mathbf a\in\{0,\ldots,d\}^{b-1}}
     \left(\prod_{j=2}^b g_{a_j}\right)
     T_{(q,\mathbf a);(p,\mathbf a)},\qquad
     g_a=x^{1-N}Q^{-a}.
 \tag{23}
\]
The same formula applies to every modified word. For the plat
presentation the original cup/cap tensors in [F] remain in its
exterior contraction. Equation (23) is not replaced by \(T_{00}\).
Each local change of coordinates (11)--(19) transports that
exterior by its inverse dual, with all pivots and Cartan factors
still attached. Hence the transformed ray-pattern contraction is
exactly the original pattern observation, even when it is zero.

The inverse dual here can be printed without an unspecified choice
of exterior. Suppose the selected crossing acts in positions
\(i,i+1\), and write the original modified word as
\(T=T_>(M\otimes I)T_<\), retaining its order.
Use \((u,v;\mathbf s)\) for the \(b\)-head vector with \(u,v\)
in those positions. Its actual exterior coefficient is
\[
 \eta_{uv;ab}=\frac1N
 \sum_{p,q,\mathbf a,\mathbf s}
   \left(\prod_{j=2}^b g_{a_j}\right)
 (T_>)_{(q,\mathbf a);(u,v;\mathbf s)}
 (T_<)_{(a,b;\mathbf s);(p,\mathbf a)} .              \tag{23b}
\]
Thus \(\nu_E(T)=\sum_{uvab}\eta_{uv;ab}M_{uv;ab}\)
before any ray integration. The corresponding cup/cap contraction
defines the same coefficient for the original plat source.
No complex conjugation is used.

Write (17) or (18) as
\(\mathcal E_\sigma(M)_\alpha
  =e_{\sigma,\mathbf k}M_{o_\sigma(\mathbf k);i_\sigma(\mathbf k)}\),
where the displayed scalar \(e_{\sigma,\mathbf k}\) includes
\(C_N,s_{05}^d,N^2\), all phases, and all four \(f\)'s.
It is nonzero on the stated regular domain. The literal
eight-face exterior is
\[
 \widehat\eta_\alpha
  =\frac{\eta_{o_\sigma(\mathbf k);i_\sigma(\mathbf k)}}
          {N^4 e_{\sigma,\mathbf k}},\qquad
 \sum_\alpha\widehat\eta_\alpha\mathcal E_\sigma(M)_\alpha
                    =\sum_{uvab}\eta_{uv;ab}M_{uv;ab}. \tag{23c}
\]
The factor \(N^{-4}\) averages exactly the four paired fibers.
On the real compact sets in (21),
\(\|\widehat\eta\|_2\) is between fixed multiples of
\(N^{-2}\|\eta\|_{\rm HS}\). This does not bound \(\eta\)
when the original remaining word has large coefficients.
Equations (23b),(23c) specify the original observation on the
new boundary, rather than assuming it agrees with a fixed cut.

For this explicit braid covector one can bound the entire all-ray
pattern. The trace norm of its first-head rank-one cut is one,
and the remaining \(b-1\) pivotal factors have trace norms \(N\).
Thus \(|\nu_E(T)|\le N^{b-1}\|T\|_2\).
If the fixed word has \(c\) crossings, (10) gives
\[
 |P_{\rm all\,ray}|
 \le |\chi_{\beta,N}|\,C_{\rm word}N^{b-1-3c}.
 \tag{23a}
\]
Here \(\chi_{\beta,N}\) is exactly the external source line of
[E,(5)], including each omitted \(\kappa^{\pm1}\) once.
It has not been renormalized. This estimates one actual whole
pattern; it supplies no relative estimate for its mixed companions.

If this supplied exterior has already been expressed as an open
physical array \(G\) with a specified covector \(\nu\), [H] gives
the explicit marked closing coupon
\[
 D_\nu=\sum_{i,j}Q^{-i}\nu_{ij}|i,j\rangle\langle i,j|,
 \qquad N^3 Z_\nu(G)=\Delta_N\nu(G).
 \tag{24}
\]
It applies to the array produced here without scalarity.
It does not identify the actual covector transported from (23)
with \(E_{00}\otimes E_{00}\).
Equations (17),(18),(23) already give a local source-preserving
replacement with its original exterior; (24) records the exact
closing once that exterior is supplied in the stated end coordinates.

## 6. The same ray chain through an actual beta elimination

There is also a specified boundary coupon when one wants to leave
the original nine-cell tensor in place and perform one of its
internal finite moves. Fix the original signed matrix \(M_0\) from
(5). Its inverse is the opposite signed matrix from that equation,
with the external \(\kappa\) convention unchanged. At fixed moment
coordinates put
\[
 D(t)_{o;o'}=\sum_{a,b=0}^d
                M(t)_{o;ab}(M_0^{-1})_{ab;o'} .       \tag{25}
\]
Every entry of both matrices on the right is given by (8), using
the chosen pattern and the original opposite pattern respectively.
The sum has only \(a+b=|o|=|o'|\), as ordinary integers.
This is an explicit finite formula for the coupon, not an assumed
bound for an inverse crossing. It has degree at most \(d\) in
each inverse moment variable, because \(M_0^{-1}\) is independent
of those variables.

For the positive array write \(u=-k_1,v=-k_2\) and
\(u'=-l_1,v'=-l_2\), with residues understood.
On its two output paired-face spaces the full coupon is
\[
 \mathscr D^+_{\alpha;\beta}(t)
 =\frac{x^{u'-u}}{N^2}
    \frac{f_1(k_1)f_2(k_2)}{f_1(l_1)f_2(l_2)}
                 D(t)_{v,u;v',u'} .                 \tag{26}
\]
The other two ports have their specified identity on the paired
image. For the negative array its output ports are 1 and 4:
\[
 \mathscr D^-_{\alpha;\beta}(t)
 =\frac{x^{\delta'-\delta}}{N^2}
    \frac{f_1(k_1)f_4(k_4)}{f_1(l_1)f_4(l_4)}
                 D(t)_{\gamma,\delta;\gamma',\delta'} ,
 \tag{27}
\]
where \((\gamma,\delta)=(-k_1,-k_4)\) and
\((\gamma',\delta')=(-l_1,-l_4)\).
Each \(N^{-2}\) averages the \(N^2\) lifts of the two input
differences. Hence (26),(27) act on the paired image and kill
the specified complementary kernel. Direct substitution into
(17),(18) gives
\[
                 \mathscr D^\sigma(t)\mathcal E_\sigma(M_0)
                     =\mathcal E_\sigma(M(t)).       \tag{28}
\]
This also proves the placement of every seam in these kernels.
Any sector change transports (26),(27) with the same port
translations; its nonconstant phase ratio must be retained.
The direct replacement bound (21) does not imply a tame norm for
(25), whose fixed inverse may have exponential norm.

Move (26) to the exterior *bilinear* covector, obtaining
\(\nu_J(t)\). This includes the original covector, all other
coupons, and their exact finite sums. Collapse only its paired
fibers:
\[
 v_J(\mathbf k;t)=
       \sum_{\alpha:\,\alpha_{m,-}-\alpha_{m,+}+h_m=k_m}
                                      \nu_J(t;\alpha).          \tag{29}
\]
There are \(N^4\) summands in (29). No constancy of the exterior
on a fiber is assumed.

Here is the first actual beta move in full. Use the canonical
nine-cell coordinates of [S,(14)--(17)] and rename its internal
variable \(t\) as \(\tau\) to distinguish it from ray coordinates.
Put
\[
 K=u+v+1,\qquad L=1-k_1+s+z,
\]
\[
 \Xi_0=u(1+\tau)+v(1+s)+(1+\tau)(1+s)
                       +z-k_1+(3h_1-1)/2.           \tag{30}
\]
Then the original pattern observation
\(\int\omega_J\sum_{\mathbf k}v_J(\mathbf k;t)B_0(\mathbf k)\)
is exactly
\[
\begin{split}
 \int\omega_J\!
 \sum_{\substack{\mathbf k,u,v,\tau,s,z\\\sum k_m=2}}
 &v_J(\mathbf k;t)\,\mathfrak n\mathfrak f_{01235}
 Q^{\Xi_0}
 W_{1234}(u)W_{1245}(v)W_{2345}(\tau)
 W_{0134}(s)W_{0145}(z)\\
 &\quad\times
 \frac{\overline W_{0235}(K+L)}
 {\overline W_{0235}(K+L-k_2)
  \overline W_{1235}(K)\overline W_{0135}(L)
  \overline W_{0345}(k_4+\tau+v+z)} .
\end{split}                                                     \tag{31}
\]
All finite indices in (31) are cyclic, and the support equation is
modulo \(N\). Here \(\mathfrak n\) and \(\mathfrak f\) are the
literal normalization factors of [S,(15)] and [C,(3)]; none has been
absorbed into the co-source. The measure \(\omega_J\) is the
product of the chosen original circle/ray measures and Gaussian
factors, with its original source lines.

For a direct proof apply [C,(9)] only to the actual \(r\)-sum
\[
 \sum_r Q^{Kr}
    \frac{W_{0123}(r)}{\overline W_{0125}(r+L)}
 =\mathfrak f_{01235}
       \frac{\overline W_{0235}(K+L)}
       {\overline W_{1235}(K)\overline W_{0135}(L)} .
 \tag{32}
\]
The exterior (29) is independent of this internal \(r\).
Deleting the \(rK\) term in [S,(17)] leaves
exactly (30), and all its other factors give (31).
In particular the two \(0235\) factors have arguments differing
by \(k_2\); their ratio is retained. They cannot be canceled
as opposite cells without an additional boundary condition.

Equation (32) is independent of every ray coordinate. The
coefficient degree bound preceding (25), and the original absolute
bound in Section 5, therefore justify its passage under the
actual integral, not just under a formal finite symbol.
At common truncated endpoints it commutes with the relative
boundary operation; the same absolute bound takes the inner
cutoffs to zero. Original lip and cap-interval seams remain
matched. Thus (31) is a source-preserving first beta move for
the full ray pattern with its exterior observation, rather than
a replacement of one internal \(W\)-factor by \(j_{\epsilon,r}\).
For another sector the source is
\(Q^{D_\chi(\mathbf k,\mathbf h)}B_0(\mathbf k)\), with
\(D_\chi\) exactly [S,(17b)]. Include this factor once in
the exterior row (29) before applying (31).
The scalar already contained in (17),(18) is not included twice.
This gives the same statement for either crossing sign and every
transported sector, without a new choice of geometric branch.

This calculation does not assign the resulting relative chain
a nonzero geometric-thimble coefficient. It supplies a concrete
analytic-current interface and retains its observation; it does
not justify deleting mixed circle/ray patterns or their cuts.
The face formulas have the complete fixed odd-level scope of their
sources; they do not assert a generic-meridian or moving-root
extension.

## Complete direct sources

- [F] [Original full-Psi scalar flow cycle](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_full_psi_scalar_flow_cycle.md),
  SHA256 692b270aa44922b930a78b25f73626b17027533d62fbec389994b51dda25c7f8.
- [E] [Literal Euler/Gaussian network](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_euler_gaussian_cauchy_network.md),
  SHA256 8ed7102043d69b442400748447dd91d1093ca1b678b6ae6acbdefaec1904317f.
- [W] [Original finite wall on the nine-cell boundary](research_actual_reciprocal_wall_nine_cell_boundary.md),
  SHA256 4a668f917a502a2aba1d6f9f2b4c2e14ef7f8c4b1f17597cd1c73080911c5d3f.
- [Q] [Braid cut and global sewing](research_braid_cut_and_global_nine_cell_sewing.md),
  SHA256 58503fba3cf834269943956429cc7ac6190499da5e40f57c82d8f13ef995b470.
- [C] [Exact nine-cell crossing evaluation](research_nine_cell_canonical_crossing_evaluation.md),
  SHA256 332062e67d64ab4a0767637c0fdd96f186d62c430ad38042aef35ad857d8d7c9.
- [S] [Literal nine-cell source and six sums](research_nine_tetrahedron_boundary_source_reduction.md),
  SHA256 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c.
- [H] [Marked cap with a prescribed observation](research_marked_cap_for_arbitrary_open_observations.md),
  SHA256 607f38636e273742f34c86f7c9ead0bdadb5c9bbe1fb2d441c22181a09e058ab.
- [A] [Uniform full-ray moments and finite inverse transport](research_uniform_full_dilogarithm_ray_transport.md),
  SHA256 5585095f56c1015cabab1409b181eabff4b4dc8fb003191881e97a38a9adf256.

No mathematical program or numerical experiment was used.
