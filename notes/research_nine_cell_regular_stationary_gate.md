# The actual nine-cell clocks and their regular stationary gate

Private written proof, 17 November 2026. The one-entry boundary
identification gives an exact dictionary from the nine-cell face
indices to the original balanced clock and shift operators. The
regular six-variable ratio phase of that same source forces every
classical boundary clock to one whenever its compatible auxiliary
shape parameters have finite nonzero limits.
Consequently its meridians are scalar in a regular commuting shift
chart. The completed source, its endpoint currents, and singular
scalings are not excluded by this result.

## 1. Exact clock and shift coordinates on the actual boundary

Let \(N>2\) be odd, \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(x=-q^{-1}\). Thus \(x^N=1\) and
\(\lambda=x^{-1}=Qx\). In [S] the primitive root called \(q\) is
our \(Q\). All finite residues below are in \(\{0,\ldots,d\}\).
Use the actual paired-face coordinates and functions of [P]:

\[
 k_m=\alpha_{m,-}-\alpha_{m,+}+h_m,\qquad
 f_m(k)=s_{0m}^{[k-1]}s_{m5}^{[-k]}.
 \tag{1}
\]

The full positive boundary array is the specified one-entry map

\[
 \mathcal E_+(M)_{\boldsymbol\alpha}
 =c_+N^2Q\,x^{b-u}\prod_m f_m(k_m)\,M_{v,u;a,b},
 \quad
 (u,v,a,b)=([-k_1],[-k_2],[k_3-1],[k_4-1]),
 \tag{2}
\]

where \(c_+=C_NQ^{\phi_+}s_{05}^d\) is retained exactly.
For the negative array the map is

\[
 \mathcal E_-(M)_{\boldsymbol\alpha}
 =c_-N^2x^{\beta-\delta}\prod_m f_m(k_m)\,
               M_{\gamma,\delta;\alpha,\beta},
 \quad
 (\gamma,\delta,\alpha,\beta)
   =([-k_1],[-k_4],[k_2-1],[k_3-1]).
 \tag{3}
\]

Here \(c_-=C_NQ^{\phi_-}s_{05}^d\), with the exact
\(\phi_-=0\) of [P]. These formulas hold for every supplied
replacement matrix. For the original signed matrix they give
the actual nine-cell boundary tensor. All paired-face fibers and
their inverse averages remain those of [P]; no cut is changed.

On functions of the four differences let
\((\mathsf T_mF)(\mathbf k)=F(\mathbf k+\mathbf e_m)\). Put

\[
 r_m(k)=\frac{f_m(k)}{f_m(k+1)}
 =\frac{s_{m5}}{s_{0m}}
   \left[1+
     \left(\frac{s_{0m}^N}{s_{m5}^N}-1\right)\delta_{k0}\right],
 \qquad
 \mathsf S_m(\mu)
   =[1+(\mu-1)\delta_{k_m0}]\,r_m(k_m)\mathsf T_m .
 \tag{4}
\]

The special factor at \(k=0\) follows from
\(f_m(0)=s_{0m}^d,\ f_m(1)=s_{m5}^d\). All other ratios
are \(s_{m5}/s_{0m}\), including the final cyclic step.
Thus (4) retains the actual root carry, not just its generic value.

Let \(Z e_j=Q^je_j\), and let \(S_\mu e_j=e_{j+1}\) for
\(j<d\), \(S_\mu e_d=\mu e_0\), with \(\mu\ne0\).
The following table gives the images of left output multiplication
and right input multiplication under (2):

\[
\begin{array}{c|cc}
 &\text{head 1}&\text{head 2}\\ \hline
 Z_{\rm out}\ (\text{left})&Q^{-k_2}&Q^{-k_1}\\
 Z_{\rm in}\ (\text{right})&Q^{k_3-1}&Q^{k_4-1}\\
 S_{\rm out}\ (\text{left})&\mathsf S_2(\mu_1)&
                                      x^{-1}\mathsf S_1(\mu_2)\\
 S_{\rm in}\ (\text{right})&\mathsf S_3(\mu_1)&
                                      x^{-1}\mathsf S_4(\mu_2)
\end{array}.
 \tag{5}
\]

For (3) the exact table is

\[
\begin{array}{c|cc}
 &\text{head 1}&\text{head 2}\\ \hline
 Z_{\rm out}\ (\text{left})&Q^{-k_1}&Q^{-k_4}\\
 Z_{\rm in}\ (\text{right})&Q^{k_2-1}&Q^{k_3-1}\\
 S_{\rm out}\ (\text{left})&\mathsf S_1(\mu_1)&
                                      x^{-1}\mathsf S_4(\mu_2)\\
 S_{\rm in}\ (\text{right})&\mathsf S_2(\mu_1)&
                                      x^{-1}\mathsf S_3(\mu_2)
\end{array}.
 \tag{6}
\]

These are identities of finite maps. For example
\((S_1M)_{v,u;a,b}\) uses \(v-1\), so it raises \(k_2\)
and contributes the ratio \(r_2\); at \(v=0\) it also contributes
the original \(\mu_1\). Replacing \(u\) by \(u-1\) similarly
raises \(k_1\), but the ratio of the two displayed
\(x^{b-u}\) phases is \(x^{-1}\). This remains true at the wrap,
because \(x^N=1\). Right multiplication raises an input index;
the same calculation proves the other two entries. Equation (3)
proves (6) with its actual port order. Right multiplication is
an opposite representation, so products of input operators keep
their original reversed action order.

In particular the actual Cartan entry \(K=xZ^{-1}\) has

\[
 K_{{\rm out},1}=xQ^{k_2}\quad\hbox{in (2)},\qquad
 Q^{-k_2}=Z_{{\rm out},1}=x/K_{{\rm out},1}.
 \tag{7}
\]

Thus the boundary multiplier in the surviving \(0235\) quotient
of [P,(31)] is an actual head clock. It is not the eigenvalue of
the peripheral meridian. The factors \(Qx^{b-u}\), the face
functions, and their seams are precisely what fixes the conjugate
shift coordinates in (5).

## 2. The original quantum Gauss data are retained by this dictionary

We use the specified original balanced meridian of [G], not a
matrix assembled from the auxiliary \(s_{ij}\). At completeness,
on each head its exact entries are

\[
 K=xZ^{-1},\qquad f=(1-Z)S_\mu,\qquad
 e=(\lambda-K)S_\mu^{-1},
 \tag{8}
\]
\[
 L_+=\begin{pmatrix}K&e\\0&1\end{pmatrix},\quad
 L_-=\begin{pmatrix}1&0\\-Kf&K\end{pmatrix},\quad
 G=L_-^{-1}L_+
     =\begin{pmatrix}K&e\\fK&fe+K^{-1}\end{pmatrix}.
 \tag{9}
\]

In [G,(1)] the possible extra endpoint in \(e\) is proportional
to \(x^{-1}-Qx\), which is exactly zero here. The products in
(8) still have their original zero endpoints; \(e\) and \(f\)
have not been cyclically replaced. Substituting the tables into
(8),(9), with the indicated ordering, therefore gives their exact
finite boundary action, including every seam in (4).

For the coupled shared flags, [G] uses
\(S_1^N=\mu,\ S_2^N=x^N\mu\). At the present odd levels these
are the same wrap, as required in its actual crossing identities.
The shared meridians are

\[
 H_1=G_1,\qquad H_2=L_{-,1}^{-1}G_2L_{-,1}.
 \tag{10}
\]

The original checked positive crossing \(M_+^0\) obeys the exact
Hurwitz identities proved in [G,(6)]:

\[
 M_+^0H_1=H_2^{\,o}M_+^0,\qquad
 M_+^0H_2=H_2^{\,o}H_1^{\,o}(H_2^{\,o})^{-1}M_+^0.
 \tag{11}
\]

The tables carry (11) to difference equations on the actual
nine-cell array by an injective change of coordinates.
No unknown conjugated meridian is introduced.
The inverse crossing has the inverse transport. A single
circle/ray replacement matrix need not satisfy (11): its original
boundary insertion and co-source in [P] remain necessary.
The statement about (11) is for the original crossing, or its
complete circle-plus-ray sum, not for each summand separately.

## 3. Exact root identities and the regular ratio phase

For every sorted tetrahedron \(i<j<k<l\), the literal shared-root
parameters of [S] are

\[
 \alpha_{ijkl}=\frac{s_{il}s_{jk}}{s_{ik}s_{jl}},
 \qquad
 \beta_{ijkl}=\frac{s_{ij}s_{kl}}{s_{ik}s_{jl}}.
 \tag{12a}
\]

The same \(s_{ij}\) is used in all cells that meet that edge.
Abbreviate the six numerator cells \(1234,1245,2345,0123,0134,0145\)
by \(u,v,t,r,s,z\), and the three denominator cells
\(0125,0235,0345\) by \(A,B,C\). Cancellation of the displayed
edge roots gives the following nine exact identities, before
taking any limit:

\[
\begin{array}{lll}
 \alpha_A=\alpha_r\alpha_s\alpha_z,&
 \alpha_B=\alpha_u\alpha_v\alpha_s\alpha_z,&
 \alpha_C=\alpha_t\alpha_v\alpha_z,\\[2pt]
 \beta_u=\beta_B\alpha_t\alpha_r,&
 \beta_v=\beta_B\beta_C\alpha_r\alpha_s,&
 \beta_t=\beta_C\alpha_u\alpha_s,\\
 \beta_r=\beta_A\alpha_u\alpha_v,&
 \beta_s=\beta_A\beta_B\alpha_v\alpha_t,&
 \beta_z=\beta_A\beta_B\beta_C.
\end{array}                                                     \tag{12b}
\]

For example the product for \(\alpha_A\) telescopes as
\[
 \frac{s_{03}s_{12}}{s_{02}s_{13}}\,
 \frac{s_{04}s_{13}}{s_{03}s_{14}}\,
 \frac{s_{05}s_{14}}{s_{04}s_{15}}
   =\frac{s_{05}s_{12}}{s_{02}s_{15}},
\]
and the first beta identity is
\[
 \frac{s_{02}s_{35}}{s_{03}s_{25}}\,
 \frac{s_{25}s_{34}}{s_{24}s_{35}}\,
 \frac{s_{03}s_{12}}{s_{02}s_{13}}
   =\frac{s_{12}s_{34}}{s_{13}s_{24}}.
\]
The other entries follow by the same literal cancellation of
(12a); thus no choice of fractional logarithm is used in (12b).

Now take any compatible level-dependent root data for which all
nine \(\alpha,\beta\) have finite nonzero limits. The symbols
\(\alpha,\beta\) below denote those limits. Use precisely the
six free indices \((u,v,t,r,s,z)\) and phase \(\Xi\) of
[S,(16),(17)]. Write their unscaled classical clocks as
\(U_0,V_0,T_0,R_0,S_0,Z_0\), and set

\[
 (U,V,T,R,S,Z)
  =(\alpha_uU_0,\alpha_vV_0,\alpha_tT_0,
     \alpha_rR_0,\alpha_sS_0,\alpha_zZ_0).
 \tag{12c}
\]

Let \(\kappa_i\) be the classical value of \(Q^{k_i}\).
The actual support \(\sum_i k_i=2\pmod N\) gives
\(\prod_i\kappa_i=1\). The three rescaled denominator arguments
are, by the first row of (12b),

\[
 A=\frac{RSZ}{\kappa_1},\qquad
 B=\frac{UVSZ}{\kappa_1\kappa_2},\qquad
 C=\kappa_4TVZ.
 \tag{12}
\]

The regular bulk domain means that all nine rescaled shapes
\(U,V,T,R,S,Z,A,B,C\) are nonzero and different from one.
The literal consecutive coefficient ratios are
\(W(j+1)/W(j)=\beta/(1-\alpha Q^{j+1})\) and
\(\bar W(j+1)/\bar W(j)=\beta/(1-\alpha Q^j)\).
Consequently the six limiting ratios of the full summand in [S]
are, in the order \(u,v,t,r,s,z\),

\[
\begin{array}{lll}
 \displaystyle
 \frac{\beta_u}{\beta_B}
       \frac{T_0R_0(1-B)}{1-U},&
 \displaystyle
 \frac{\beta_v}{\beta_B\beta_C}
       \frac{R_0S_0(1-B)(1-C)}{1-V},&
 \displaystyle
 \frac{\beta_t}{\beta_C}
       \frac{U_0S_0(1-C)}{1-T},\\[6pt]
 \displaystyle
 \frac{\beta_r}{\beta_A}
       \frac{U_0V_0(1-A)}{1-R},&
 \displaystyle
 \frac{\beta_s}{\beta_A\beta_B}
       \frac{V_0T_0(1-A)(1-B)}{1-S},&
 \displaystyle
 \frac{\beta_z}{\beta_A\beta_B\beta_C}
       \frac{(1-A)(1-B)(1-C)}{1-Z}.
\end{array}                                                     \tag{12d}
\]

The six beta identities in (12b) cancel every coefficient
introduced by the rescaling (12c). On a local logarithmic lift,
a primitive for the resulting universal ratios is therefore

\[
\begin{split}
 \mathscr S={}&
 \operatorname{Li}_2(U)+\operatorname{Li}_2(V)
 +\operatorname{Li}_2(T)+\operatorname{Li}_2(R)
 +\operatorname{Li}_2(S)+\operatorname{Li}_2(Z)\\
 &-\operatorname{Li}_2(A)-\operatorname{Li}_2(B)
  -\operatorname{Li}_2(C)\\
 &+\Log U\Log T+\Log U\Log R+\Log V\Log R
   +\Log V\Log S+\Log T\Log S .
\end{split}                                                     \tag{13}
\]

Its derivatives are logarithms of the six ratios; changing their
lift adds the corresponding integral \(2\pi i\) linear marks and
an additive constant. In particular this includes the fixed-log
choice \(s_{ij}(N)=\exp(\ell_{ij}/N)\), for which
\(\alpha,\beta\to1\). It also includes other shared-root scalings
with finite nonzero limits, without an asymptotic estimate for
the associated Pochhammer products.

The finite \(+1,+2\) arguments and the linear part of \(\Xi\)
are retained in the original source, but disappear from these
leading internal equations. The full normalization is independent
of all six internal indices and hence does not alter them.
The prescribed sector change in [S,(17a),(17b)] is also independent
of those indices after its literal affine reindexing. In particular
the bounded port translations for the two signed conventions
(2),(3) do not change the classical clocks or this internal gate.
Equations (12d),(13) specify the regular logarithmic-ratio phase;
it does not select a contour or assert a stationary approximation
to the finite sum. Logarithmic aliases change its derivatives by
the corresponding integer \(2\pi i\) marks. Every stationary lift
therefore satisfies the following exponentiated equations:

\[
\begin{array}{ll}
1-U=TR(1-B),&
1-V=RS(1-B)(1-C),\\
1-T=US(1-C),&
1-R=UV(1-A),\\
1-S=VT(1-A)(1-B),&
1-Z=(1-A)(1-B)(1-C).
\end{array}                                                     \tag{14}
\]

The denominator incidence matters here: \(B\) contains \(V\) but
not \(R\), and \(C\) also contains \(V\). These are the literal
arguments in [S,(16)], not a symmetric surrogate.

## 4. Elimination and the boundary-clock gate

Every regular solution of (12),(14) satisfies

\[
                    \kappa_1=\kappa_2=\kappa_3=\kappa_4=1.
 \tag{15}
\]

Here is an explicit elimination. Set \(a=1-A,\ b=1-B,\ c=1-C\);
these letters are temporary and do not denote head indices.
Comparing the \(S,R,U\) equations in (14) gives
\(URS=U+R-1\). Comparing its \(V,T,U\) equations gives
\(UTV=U+T-1\). Thus

\[
 V=\frac{U+T-1}{UT},\qquad
 S=\frac{U+R-1}{UR}.
 \tag{16}
\]

The two numerators here are nonzero because \(V,S,U,T,R\ne0\).
Put \(F=U-1+TR\). Now the \(R,U,T\) equations give

\[
 A=\frac{F}{U+T-1},\qquad
 B=\frac{F}{TR},\qquad
 C=\frac{F}{U+R-1}.
 \tag{17}
\]

In particular \(F\ne0\), since \(B\ne0\).
The last equation in (14) becomes

\[
 1-Z=\frac{(1-R)(1-U)(1-T)}
                  {(U+T-1)(U+R-1)},\qquad
 Z=\frac{UF}{(U+T-1)(U+R-1)}.
 \tag{18}
\]

For the second equality expand the numerator
\((U+T-1)(U+R-1)-(1-R)(1-U)(1-T)=UF\).
Equations (16)--(18) imply the three exact monomial identities

\[
                         RSZ=A,\qquad UVSZ=B,\qquad TVZ=C.
 \tag{19}
\]

Comparison with (12) first gives
\(\kappa_1=1,\ \kappa_1\kappa_2=1,\ \kappa_4=1\).
The boundary support then gives \(\kappa_3=1\).
No division by an extra expression outside the stated regular
domain has been used. This proves (15) on every logarithmic alias.

In particular the two \(0235\) factors retained after the first
beta move have classical arguments \(w\) and \(w/\kappa_2\).
The local move permits their cancellation only on the gate
\(\kappa_2=1\); away from it their continued primitive difference
\(\operatorname{Li}_2(w)-\operatorname{Li}_2(w/\kappa_2)\)
is part of the actual source. The six-equation calculation shows
that this equal-shape condition is forced by regular interior
stationarity, not by the finite beta identity on arbitrary data.

## 5. Consequence for the actual meridians and precise scope

By the exact tables, (15) makes every classical input and output
clock \(Z_i\) equal to one, for either signed port convention.
The factors \(Q^{-1}\) in the input clocks tend to one.
This does not say that the finite residues \(k_i\) are zero:
different residue endpoints and their original carries remain
distinct in the finite source.

Suppose in addition that the original shifts have finite nonzero
commuting symbols \(s_i\). This is the regular torus chart for
the actual cyclic completions, not a normalization of the
nilpotent \(e_i\). In this chart \(x,\lambda\to-1\), and
(8),(9) have the explicit classical form

\[
 K=-Z^{-1},\quad e=\frac{-1-K}{s},\quad f=(1-Z)s,
 \qquad
 G=\begin{pmatrix}
 K&-(K+1)/s\\
 (K+1)s&-K-2
 \end{pmatrix}.
 \tag{20}
\]

Thus \(Z=1\) gives \(G=-I\). The shared conjugation in (10)
does not change this scalar matrix. Therefore a regular interior
critical point of the specified six-variable chart cannot
represent a nontrivial boundary-parabolic meridian in these
actual balanced Gauss coordinates.

This is a gate for this literal ratio phase throughout the stated
finite nonzero root-limit regime. It does not show that
the original finite source has zero geometric contribution.
An endpoint or collision contribution, a shift symbol tending
to zero or infinity, or auxiliary shape parameters with zero,
infinite, or nonconvergent limits are outside this regular chart.
Changing compatible auxiliary root branches while keeping finite
nonzero limits does not evade (12b)--(15). The full relative
moment rays, beta endpoint currents, original cap, and normal
jets are not removed. In particular the proven finite source
comparison cannot be replaced by an assertion that the ordinary
interior stationary points of its nine-cell phase already supply
the desired geometric cycle. The gate directs that comparison to its retained boundary
and singular charts; it proves no volume-conjecture counterexample
or failure of a suitably completed geometric transport.

## Complete direct sources

- [S] [Literal nine-cell source and six sums](research_nine_tetrahedron_boundary_source_reduction.md),
  SHA256 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c.
- [P] [Actual ray-pattern boundary maps](research_full_psi_ray_crossings_and_nine_cell_boundary.md),
  SHA256 495a2fde1ed1d7ca0707f060208121bddb2673be21ff3bcb9bac737420ac2d24.
- [G] [Original shared quantum flags](actual_shared_quantum_flags_and_charged_exchange.md),
  SHA256 dcab795cc141e2e1db726998cf7b1141dd03c681eaae9076387f90581f53a7d9.

All three complete texts were read and the used implications checked.
No mathematical program or numerical experiment was used.
