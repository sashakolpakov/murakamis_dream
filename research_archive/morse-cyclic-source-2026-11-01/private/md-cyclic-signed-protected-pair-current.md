# The signed current of an actual adjacent bipyramidal pair

The opposite-offset bipyramid has an exact two-box coefficient kernel with both exterior demands retained. It is not the aligned cap/CROSS contraction. The difference is visible in a finite Green identity: the aligned reflection cancels the interior current, whereas the actual opposite-offset shift leaves four bands. This note proves the kernel and the resulting finite clock recurrence. It makes no estimate of the full complementary source and no volume assertion.

All matrices below are the actual polynomial face matrices. No independent absolute local envelope is substituted. The current identity holds at repeated spectral nodes, at coincident spectral parameters, and at both level parities.

## 1. The literal adjacent boxes and their exterior demands

Use the oriented bipyramidal source with even \(m\ge6\), north spokes matched at odd indices, south spokes matched at even indices, and protected original mark \(Nz_0\). At the marked north box \(j=1\) and the next south box \(j=2\), put \(Y=z_1\), \(Z=z_2\), \(B=z_3\). Their actual ordered factors are
\[
 H_{V,\mathrm L}(0,0,Z,Y;\sigma),
 \qquad H_{V,\mathrm C}(S,B,Y,Z;\tau).
 \tag{1}
\]
The north factor in (1) is its LEFT part; the south factor is its CROSS part. Their common spectral parameters remain independent. Here \(S\) is the single south-pole face variable, shared with the other south boxes.

Let \(\alpha\) be the degree supplied to \(Y\) by the box \(j=0\), and let \(\beta\) be the degree supplied to \(Z\) by the box \(j=3\). These are actual exterior degrees, not independently chosen replacement targets. The pair therefore supplies the coefficient
\[
 \mathcal B_{\alpha,\beta}(S,B;\sigma,\tau)
  =[Y^{d-\alpha}Z^{d-\beta}]
       H_{V,\mathrm L}(0,0,Z,Y;\sigma)
       H_{V,\mathrm C}(S,B,Y,Z;\tau),
 \qquad d=N-1.
 \tag{2}
\]
The remainder of the cyclic contraction retains its original \(S\)- and \(B\)-demands. In particular (2) must not be evaluated at separate optimized values of \(S\) or \(B\).

Put
\[
 Q=q^2,\quad q=e^{\pi i/N},\quad
 c_r=qQ^r+q^{-1}Q^{-r},\quad
 a_r=2-Q^r-Q^{-r}=4\sin^2\frac{\pi r}{N},
 \tag{3}
\]
\[
 b_r=q+q^{-1}-q^{-1}Q^r-qQ^{-r}
      =4\sin\frac{\pi r}{N}\sin\frac{\pi(r-1)}{N}.
 \tag{4}
\]
The original face Casimir at outer variables \(S,1\), acting by columns on \(1,z,\ldots,z^d\), is
\[
 C(S)z^r=c_rz^r-a_r(1+S)z^{r-1}-b_rS z^{r-2},
 \qquad C=C(0).
 \tag{5}
\]
The endpoint coefficients \(a_0=a_N=b_0=b_1=b_N=b_{N+1}=0\) implement every missing arrow that is used below.

Let
\[
 \chi_N(t)=2T_N(t/2)+2,\quad
 A(\sigma)=V_N(\sigma;C),\quad
 B(\tau,S)=V_N(\tau;C(S)),
 \qquad V_N(t;C)=\chi_N(t)(tI-C)^{-1}.
 \tag{6}
\]
The last expression denotes its polynomial continuation. These matrices satisfy both left and right cleared-resolvent equations, since their full characteristic polynomial is \(\chi_N\). Set
\[
 v_l(\sigma)=A(\sigma)_{0,l},\qquad
 B_{i,j,p}(\tau)=[S^p]B(\tau,S)_{i,j}.
 \tag{7}
\]

Homogeneity in (2) forces \(i+p=\alpha+\beta\) for the coefficient of \(B^iS^p\). The exact coefficient is
\[
 [B^iS^p]\mathcal B_{\alpha,\beta}
       =\sum_{l=L}^{U}v_l(\sigma)B_{i,l+\alpha,p}(\tau),
 \tag{8}
\]
where
\[
 \begin{split}
 h&=\lfloor d/2\rfloor,\qquad M=\lfloor N/2\rfloor-1,\\
 L&=\max\{0,\beta,\lfloor N/2\rfloor-\alpha\},\\
 U&=\min\{M,d-\alpha\}.
 \end{split}
 \tag{9}
\]
It is zero unless \(0\le i\le h\), \(p\ge0\), \(i+p=\alpha+\beta\), and \(L\le U\).

To prove this, the first factor contributes \(v_lY^lZ^{d-l}\), with \(0\le l\le M\). In the second factor let \(j\) be its input monomial degree and \(i\) its output middle degree. Its monomial is
\(S^pB^iY^{d-j}Z^{j-i-p}\).
The two demands in (2) give \(j=l+\alpha\) and \(i+p=\alpha+\beta\). The remaining \(Z\)-degree is \(l-\beta\), so \(l\ge\beta\). The original CROSS support is \(i\le h\), \(j\ge\lfloor N/2\rfloor\), and \(j\le d\), giving exactly (9). At odd \(N\), the central row stays in CROSS. This argument neither divides out its zero nor changes the cutoff.

## 2. A finite kernel with an explicit depth clock

Fix an interval \(I=[L,U]\subseteq[0,d]\), initially without choosing it from (9). Let \(P_I\) be its diagonal projector. Let \(U_\alpha\) be the finite shift matrix
\[
 (U_\alpha)_{l,j}=\mathbf1_{\{j=l+\alpha,\ 0\le l,j\le d\}},
 \qquad
 Z(z)=\operatorname{diag}(1,z,\ldots,z^d).
 \tag{10}
\]
The finite clock \(z\) records the original north depth. Define
\[
 K_{\alpha,i,I}(z,S;\sigma,\tau)
   =e_0^{\mathsf T}A(\sigma)P_IZ(z)U_\alpha
                         B(\tau,S)^{\mathsf T}e_i
   =\sum_{l\in I}z^lv_l(\sigma)B(\tau,S)_{i,l+\alpha}.
 \tag{11}
\]
Out-of-range matrix indices mean zero. Formula (8) is
\([S^p]K_{\alpha,i,I}(1,S;\sigma,\tau)\) with the literal interval (9).
The extra clock does not change the source. It retains phase information needed to close the finite recurrence.

For a polynomial \(F(z)\), write
\[
 \mathcal T_+F(z)=F(Qz),\qquad
 \mathcal T_-F(z)=F(Q^{-1}z).
 \tag{12}
\]
Define the finite clock operators
\[
 \begin{split}
 \mathcal D_\alpha
     &=q(1-Q^\alpha)\mathcal T_+
          +q^{-1}(1-Q^{-\alpha})\mathcal T_-,\\
 \mathcal A_r
     &=2-Q^r\mathcal T_+-Q^{-r}\mathcal T_-,\\
 \mathcal B_r
     &=q+q^{-1}-q^{-1}Q^r\mathcal T_+
                              -qQ^{-r}\mathcal T_-.
 \end{split}
 \tag{13}
\]
For example \(\mathcal A_r\) multiplies the \(z^l\) coefficient by \(a_{l+r}\). These operators preserve every original root phase.

## 3. The root-safe Green identity

Suppress \(i,I,\sigma,\tau\) in the notation \(K_\alpha\). Then
\[
 \begin{split}
 (\sigma-\tau)K_\alpha
 ={}&F_{\alpha,i,I}
     +\mathcal D_\alpha K_\alpha
     -z\mathcal A_1K_{\alpha+1}\\
    &+(1+S)\mathcal A_\alpha K_{\alpha-1}
      +S\mathcal B_\alpha K_{\alpha-2}
      +E_{\alpha,i,I},
 \end{split}
 \tag{14}
\]
where all kernels on the right have the **same fixed interval \(I\)**. The two resolvent forcing terms are
\[
 F_{\alpha,i,I}
  =\chi_N(\sigma)\mathbf1_{\{0\in I\}}B(\tau,S)_{i,\alpha}
    -\chi_N(\tau)\mathbf1_{\{i-\alpha\in I\}}
                    z^{i-\alpha}v_{i-\alpha}(\sigma),
 \tag{15}
\]
and both cutoff currents are retained:
\[
 \begin{split}
 E_{\alpha,i,I}
  ={}&-a_Lz^Lv_{L-1}(\sigma)B(\tau,S)_{i,L+\alpha}\\
     &+a_{U+1}z^{U+1}v_U(\sigma)
                         B(\tau,S)_{i,U+1+\alpha}.
 \end{split}
 \tag{16}
\]
The stated endpoint convention makes (16) valid at \(L=0\) and \(U=d\). Equation (14) is a polynomial identity. There is no division by \(\sigma-\tau\), so it remains valid on the coincident-spectrum diagonal and at every root normal.

For the proof, use the two cleared-resolvent equations on the matrix product to obtain
\[
 \begin{split}
 (\sigma-\tau)AP_IZU_\alpha B^{\mathsf T}
 ={}&\chi_N(\sigma)P_IZU_\alpha B^{\mathsf T}
       -\chi_N(\tau)AP_IZU_\alpha\\
    &+A\{CP_IZU_\alpha-P_IZU_\alpha C(S)^{\mathsf T}\}
                                                 B^{\mathsf T}.
 \end{split}
 \tag{17}
\]
The projector commutator is exactly
\[
 [C,P_I]
        =-a_LE_{L-1,L}+a_{U+1}E_{U,U+1}.
 \tag{18}
\]
This gives (16). In the remaining term factor the row weight \(z^l\). The four possible column offsets from \(l\) are \(\alpha,\alpha+1,\alpha-1,\alpha-2\), with coefficients
\[
 c_l-c_{l+\alpha},\qquad
 -za_{l+1},\qquad
 (1+S)a_{l+\alpha},\qquad
 Sb_{l+\alpha}.
 \tag{19}
\]
The formulas (3), (4) turn these coefficient multipliers into (13), proving (14). The physical endpoint zeros in (5) also justify the calculation when a shifted index lies just outside the matrix.

Taking the coefficient of \(S^p\) gives a finite recurrence that retains the south degree:
\[
 \begin{split}
 (\sigma-\tau)K_{\alpha,p}
 ={}&F_{\alpha,p}+\mathcal D_\alpha K_{\alpha,p}
          -z\mathcal A_1K_{\alpha+1,p}\\
    &+\mathcal A_\alpha
           (K_{\alpha-1,p}+K_{\alpha-1,p-1})
          +\mathcal B_\alpha K_{\alpha-2,p-1}
          +E_{\alpha,p}.
 \end{split}
 \tag{20}
\]
Negative \(p\) means zero. There are finitely many degrees \(p\), and the clock shifts are periodic modulo \(N\). No infinite Fourier series is used.

One cannot change the cutoff on each neighboring \(K_{\alpha\pm r,p}\) to the interval that would arise from a different actual exterior load without adding the corresponding finite interval-difference terms. Formula (20) uses one fixed interval throughout. This is necessary to retain all projected endpoint currents.

## 4. Why the aligned telescope does not sew unchanged

Let \(J\) reverse the complete range \(0,\ldots,d\). Exact root reflection gives \(CJ=JC^{\mathsf T}\). Consequently the unprojected complementary-index kernel
\(A(\sigma)JB(\tau,0)^{\mathsf T}\)
obeys a resolvent difference identity without an interior current. With a cutoff, only the finite commutator \([C,P_I]J\) remains. This is the mechanism behind the aligned two-row telescope: its indices are complementary.

The actual opposite-offset pair (1) instead has the shift \(U_\alpha\). Even before the cutoff, its interior current at \(z=1\) is
\[
                  CU_\alpha-U_\alpha C(S)^{\mathsf T}.
 \tag{21}
\]
It is exactly the four-band matrix (19), with \(z=1\). It does not vanish in general. For instance \(\alpha=0,S=0\) gives \(C-C^{\mathsf T}\), whose first off-diagonal entries are \(-a_1,a_1\ne0\). That example describes the full unprojected kernel; the actual LEFT/CROSS block has its additional interval (9). The example is not asserted to be a nonzero admissible LEFT/CROSS sector at \(\alpha=0\).

Nor does the depth clock disappear from (20): evaluating the original source at \(z=1\) couples it to the actual values at \(Q,Q^{-1}\). Dropping those phases changes the finite identity. Thus a direct reuse of the aligned endpoint telescope would omit a genuine interior term as well as, potentially, a cutoff current.

## 5. The interior current need not disappear after the actual shared extraction

This can be checked exactly without any asymptotic estimate. First use the full north and south coupons, rather than their projections in (1), and take \(I=[0,d]\) in (17). Its two endpoint currents vanish. Contract this identity with the entire remaining original bipyramidal source, including every ordinary face demand. Write \(\mathscr S_N\) for this multilinear marked source, and let \(\mathscr S_N^{(1:I)}\), \(\mathscr S_N^{(2:I)}\) mean that the indicated coupon is replaced by the identity polynomial. The globally sewn interior current is exactly
\[
 G_N=(\sigma-\tau)\mathscr S_N
       -\chi_N(\sigma)\mathscr S_N^{(1:I)}
       +\chi_N(\tau)\mathscr S_N^{(2:I)}.
 \tag{22}
\]
Equivalently it is the original shared source with \(C V_N(\sigma;C)\) inserted at the north box, minus the source with \(C V_N(\tau;C)\) inserted at the south box. These are insertions at their respective actual pairs; they are not silently identified.

At \(N=3\), \(m=6\), take the actual ordered spectral tuple
\((2,0,2,2,2,2)\), so \(\sigma=0\), \(\tau=2\). The full original homogeneous source and the two identity replacements are
\[
 \mathscr S_3=910845,\qquad
 \mathscr S_3^{(1:I)}=115587,\qquad
 \mathscr S_3^{(2:I)}=243.
 \tag{23}
\]
These integers follow by multiplying the six literal homogeneous polynomials and extracting \(S^2z_1^2\cdots z_5^2\), with north and \(z_0\) protected. Here
\[
 C(S)=
 \begin{pmatrix}
 1&-3(1+S)&-3S\\
 0&-2&-3(1+S)\\
 0&0&1
 \end{pmatrix},
 \qquad V_3(t;C)=C^2+tC+(t^2-3)I.
 \tag{24}
\]
Thus the input data involve only exact integer arithmetic. Since
\(\chi_3(t)=t^3-3t+2\), equation (22) gives
\[
                    G_3=-2051892\ne0.
 \tag{25}
\]
The same result is obtained by the two direct \(C V_3\) insertions, without using (22). The private checker records both constructions. This disproves automatic disappearance of this interior current after the full original shared extraction. It is not a counterexample to the desired strict bound for \(D_N\).

The elementary root Ward identity is consistent with this result. Define
\(Dz^j=2\sin(j\pi/N)z^{j-1}\) and \(E_qf(z)=f(qz)\). Then
\[
 D(fg)=(Df)(E_qg)+(E_q^{-1}f)(Dg),
 \qquad [z^d]DP=0
 \tag{26}
\]
for every polynomial \(P\), because the only possible contribution comes from its \(z^N\) coefficient and \(\sin\pi=0\). At an ordinary equatorial face there are three incident coupons, so the corresponding exact divergence reads
\[
 [z^d]\left\{
 (Df)(E_qg)(E_qh)
 +(E_q^{-1}f)(Dg)(E_qh)
 +(E_q^{-1}f)(E_q^{-1}g)(Dh)\right\}=0.
 \tag{27}
\]
The spectator factors are shifted. Moving a derivative from the chosen pair onto the remaining source therefore leaves those shifts and spectator insertions; it does not give a zero for (22). Any use of (27) in a cyclic estimate must retain them.

## 6. What this identity leaves to prove

Formula (20) supplies a finite recurrence for the actual two-box block with both exterior demands and every south-degree coefficient present. A global proof could seek cancellation of these interior currents after the remaining cyclic source is contracted, or a quantitative signed bound on that contraction. Neither conclusion follows merely from the nonincreasing grade count.

The required global estimate is still for the original unsplit difference
\(D_N=S_N^{\mathrm{full}}-S_N^{\mathrm{CROSS}}\):
\[
       \|D_N\|_{[-2,2]^m}
          \le
       \exp\{N(\operatorname{Vol}(Y)/(2\pi)-\eta+o(1))\},
       \qquad \eta>0.
 \tag{28}
\]
It must keep one common south-pole demand and all original equatorial demands. The exact finite filling norm adds no exponential cost to (28), but cannot supply it. The all-CROSS nonzero filling asymptotic and its applicability to the literal bipyramid are supplied separately by [the general Morse geometric contribution](https://sashakolpakov.github.io/murakamis_dream/notes/actual_morse_geometric_contribution.html). That theorem does not prove (28). This note proves no new volume limit.
