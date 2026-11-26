# The complete 44 message on a second-period seam collar

Private written proof, 11 November 2026. The finite-source estimate
below retains the entire first contraction and both second Fourier
alternatives. Its calibration uses the original three-factor affine
action and its outgoing halfweight, through the separately proved
formal-action floor.

The proof bounds a fixed complex neighborhood of \(Y=1\), hence
short continuous pieces near both ends of the second period. It does
not infer a collar from the single value at \(Y=1\), replace the
complete message by its local packet, or estimate the second
complement away from this collar.

## 1. Original source and target

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(443\) or \(444\), with flags \((1,1,\beta)\), \(\beta=0,1\).
Retain its original coupled reference \(r_j\), absolute action,
logarithmic lifts, and ordinary incoming color \(w\). Put
\[
 P=[11/50,9/20],\qquad z=v+ic_3,\quad v\in P,\quad c_3=\Im r_3,
 \qquad Z=e^{-2\pi iz}.
 \tag{1}
\]
The established actual ordinary-image bounds give
\[
 \begin{array}{c|c}
 \beta=0&-13/200\le c_3\le17/250,\\
 \beta=1&-51/500\le c_3\le-1/1000.
 \end{array}
 \tag{2}
\]
They apply to the third retained coordinate also when \(m=4\);
there its following leg is attached. No terminal private index is
substituted for the third ordinary conditional index.

With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), \(S_j=|P_j|\), and
\(p_j(X)=(rX;r)_j\), keep the literal functions
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
                   H_N(w,r^{-i})p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
                   X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon},\\
 f_N(w,Y)&=f_{44,N}(w,Y)\\
 &=N\operatorname{CT}_X
   [U_{1,N}(w,X)d_N(X)(1+X^{-N})C_{1,N}(X,Y)].
\end{split}
 \tag{3}
\]
The endpoint coefficient is complete, and \(d_N(r^j)=P_j^{-1}\)
with \(\deg d_N<N\). The exact first-period identity is
\[
 f_N(w,Y)=\sum_{a=0}^{N-1}
                  \frac{U_{1,N}(w,r^a)}{P_a}C_{1,N}(r^a,Y).
 \tag{4}
\]
This is the unnormalized physical sum of the pointwise prefix
theorem. There is no extra factor two, root average, or outgoing
diagonal polynomial in (4).

For the second sector \(\sigma=0,1\), define the holomorphic density
\[
 \mathscr D_{\sigma,\beta,N}(w,Y,Z)
       =f_N(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z).
 \tag{5}
\]
Its second extraction measure remains \(+N\,dy\), with
\(Y=e^{-2\pi iy}\). Carry the third allocation
\[
 D_{\beta,N}(Z)=
 \begin{cases}1,&\beta=0,\\ |d_N(Z)|^{1/2},&\beta=1.\end{cases}
 \tag{6}
\]
This is a nonnegative multiplier, including at its zeros.

Let \(\Lambda_{123}(z)\) be the unchanged affine action of the
second-selected source. Equivalently, with the original cap phase
\(\Psi\) and conditional phases \(Q_\epsilon\),
\[
\begin{split}
 F_{123}
 &=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)+Q_\beta(s_3;z_2,z_3)\\
 &\hspace{1em}-g(z_1)-g(z_2)-\frac{\beta}{2}g(z_3),\\
 \Lambda_{123}(z)
 &=\Re F_{123,*}+\Re\{p_R(z-r_3)\},\\
 p_R&=g'(s_3^*+r_3)-(1+\beta/2)g'(r_3).
\end{split}
 \tag{7}
\]
Every star refers to this same actual word.

**Theorem.** For this fixed actual word there are
\(\varepsilon>0\), a fixed ordinary-color disk
\(\mathcal D\) about \(-2\), and constants \(C,B,N_0\) such that,
at both level parities and \(N\ge N_0\),
\[
 |\mathscr D_{\sigma,\beta,N}(w,Y,Z)|D_{\beta,N}(Z)
       \le C N^B
          e^{N\{\Lambda_{123}(z)-1/500\}},
 \quad |Y-1|\le2\varepsilon,\quad
 w\in[-2,2]\cup\mathcal D,\quad z\ \hbox{as in (1)}.
 \tag{7a}
\]
Both second Fourier choices \(\sigma=0,1\) satisfy this same
bound. Every fixed number of \(Y\) and ordinary-color derivatives
has the same exponential rate on \(|Y-1|\le\varepsilon\) and
smaller color disks, with a possibly different polynomial prefactor.
The outgoing multiplier is not differentiated.

In particular, the original second integration with density
\(+N\,dy\) has a strict gap on fixed small complex neighborhoods
of \(y=0\) and \(y=1\). No collar width independent of the fixed
word is asserted. The intervening second arcs and their height
connections are not part of the theorem.

## 2. Two exact finite seam bounds

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 g(t)=J(t)+\frac{\pi i}{2}(t-t^2),\qquad
 c_{\rm b}=-2J(1/6)<13/40,\qquad b_1=433/500 .
 \tag{8}
\]
The rational inequality in (8) is proved in Section 2 of the
complete-source seam theorem. Uniform sine-factorial bounds give
\[
 \log S_j=NJ(j/N)+O(\log N),\qquad
                  |J(t)|\le c_{\rm b}/2\quad(0\le t\le1).
 \tag{9}
\]
The whole coherent coefficient norm is
\[
 \sum_{i<N}\frac{|H_N(w,r^{-i})|}{S_i}
       \le C_\tau N^{B_\tau}e^{N(b_1+\tau)} .
 \tag{10}
\]
Lemma 2 of terminal real-color decay proves (10) on the whole real
ordinary-color interval. The cap seam theorem gives its fixed
complex-color version with an arbitrary prescribed rate allowance.
Both include the literal endpoint groups and both level parities.
No individual Newton summands inside \(H_N\) replace it.

For \(|X|=1\), the finite binomial identity in
[the physical-end source, equation (4)](research_mixed_three_four_next_first_physical_end.md)
gives
\[
 \frac{p_i(X)}{P_i}
  =\sum_{k=0}^i
      \frac{(-1)^k r^{k(k+1)/2}X^k}{P_kP_{i-k}},
 \qquad
 \frac{|p_i(X)|}{S_i}\le C N^B e^{Nc_{\rm b}} .
 \tag{11}
\]
All denominator indices are less than \(N\); (9) proves the last
bound, uniformly through the two ends. Thus the literal full cap
obeys
\[
 \sup_{|X|=1}|U_{1,N}(w,X)|
       \le C_\tau N^{B_\tau}e^{N(b_1+c_{\rm b}+\tau)}.
 \tag{12}
\]

The whole diagonal polynomial, on the same entire circle, satisfies
\[
                    \sup_{|X|=1}|d_N(X)|
                         \le C N^B e^{Nc_{\rm b}/2}.
 \tag{13}
\]
Indeed its exact cardinal expansion is
\[
 d_N(X)=\sum_{a<N}\frac{\mathfrak l_a(X)}{P_a},\qquad
 \mathfrak l_a(X)=\frac1N\sum_{k=0}^{N-1}(Xr^{-a})^k.
 \tag{14}
\]
Every cardinal polynomial has modulus at most one on \(|X|=1\).
Equation (9) therefore proves (13). This proof includes \(X=1\)
and every physical node; it does not apply a compact-strip
factorial approximation at a strip endpoint.

For \(0<\varepsilon<1\), put
\[
 \mathcal V_\varepsilon=\{Y:|Y-1|\le\varepsilon\},\qquad
 \Omega(\varepsilon)=
 \log(1+\varepsilon/2)
       +\frac{\varepsilon}{2}\log(1+2/\varepsilon).
 \tag{15}
\]
The exact finite inequality from the complete-source seam theorem is
\[
       \frac{|p_j(Y)|}{S_j}\le e^{N\Omega(\varepsilon)}
                 \quad(j<N,\ Y\in\mathcal V_\varepsilon).
 \tag{16}
\]
For completeness, each factor of this quotient is at most
\(1+\varepsilon/|1-r^k|\). The sine chord gives
\(|1-r^k|\ge4\min(k/N,1-k/N)\). Pairing the two ends and
integrating the decreasing logarithm proves
\[
 \sum_{k=1}^{N-1}
       \log\left(1+\frac{\varepsilon}{|1-r^k|}\right)
 \le 2N\int_0^{1/2}\log(1+\varepsilon/(4t))\,dt
 =N\Omega(\varepsilon).
 \tag{17}
\]
At even levels this harmlessly counts the middle factor twice.
Every shorter product is bounded by the same positive full product.
In particular \(\Omega(\varepsilon)\to0\).

The separate exact identity
\[
 d_N(Y)=\frac1N C_{0,N}(1,Y)
       =\frac1N\sum_{j<N}\frac{p_j(Y)}{P_j}
 \tag{18}
\]
therefore gives \(|d_N(Y)|\le e^{N\Omega(\varepsilon)}\)
on this collar. The endpoint forcing of \(d_N\) is retained.
Also, for every \(j<N\) and \(\sigma=0,1\),
\[
 |Y^{-j}|,\ |Y^{-\sigma N}|
                   \le e^{-N\log(1-\varepsilon)}.
 \tag{19}
\]

## 3. The complete first contraction on the collar

Use the original full-disk row norm
\[
 \sup_{|X|\le1}\sum_{j<N}\frac{|p_j(X)|}{S_j^2}
        \le C_\tau N^{B_\tau}e^{N(7/15+\tau)}.
 \tag{20}
\]
This is equations (13)--(15) of the transformed real-initial
source. Its proof bounds every literal numerator and denominator,
including all endpoint rows. On \(|X|=1\), (16) and (20) imply
\[
 |C_{1,N}(X,Y)|
 \le C_\tau N^{B_\tau}
            e^{N\{7/15+\Omega(\varepsilon)+\tau\}}.
 \tag{21}
\]
There is no physical termination in either variable in this step.

Take the first coefficient in (3) on the full real first period.
On that circle \(|1+X^{-N}|\le2\). Equations (12), (13), and
(21), including the original \(N\) extraction density, give
\[
 |f_N(w,Y)|\le C_\tau N^{B_\tau}
      e^{N\{B_{44}+\Omega(\varepsilon)+\tau\}},\qquad
 B_{44}=b_1+\frac32c_{\rm b}+\frac7{15}.
 \tag{22}
\]
The factor two here comes only from taking a modulus of the two
Fourier summands. It does not modify the exact physical sum (4).
In particular (22) has not dropped the first diagonal polynomial
or its selected alternative. It is valid throughout the complex
collar before the second integration is performed.

## 4. Attach the complete next conditional source

For a fixed output radius \(R\), define
\[
\begin{split}
 L(t)&=-2J((1-t)/2),\\
 M_\beta(C)&=\max_{0\le t\le1}
                 \{L(t)-(1+\beta)J(t)+Ct\}.
\end{split}
 \tag{23}
\]
The full numerator and sine-factorial estimates give
\[
 \sup_{|Z|\le R}\sum_{j<N}\frac{|p_j(Z)|}{S_j^{1+\beta}}
 \le C_\tau N^{B_\tau}e^{N\{M_\beta(\log_+R)+\tau\}}.
 \tag{24}
\]
The written bounds in the low-index kernel margin are
\[
 m_0=\frac{1271}{2500}>M_0(17\pi/125),\qquad
 m_1=\frac7{15}>M_1(0).
 \tag{25}
\]
By (2), the respective disks in (25) contain all present output
targets \(Z\). Only this all-row estimate is used from that
low-index source; its separate statement about physical incoming
support is not imposed on the current complex \(Y\).

From (16), (19), and (24)--(25), directly in the original finite
conditional sum,
\[
 |C_{\beta,N}(Y,Z)|
 \le C_\tau N^{B_\tau}
 e^{N\{m_\beta+\Omega(\varepsilon)
                         -\log(1-\varepsilon)+\tau\}} .
 \tag{26}
\]
Every revived and wrapped row through \(N-1\) is included.
Combining (18), (19), (22), and (26) proves the unallocated
complete-density bound
\[
 |\mathscr D_{\sigma,\beta,N}(w,Y,Z)|
 \le C_\tau N^{B_\tau}
       e^{N\{B_{44}+m_\beta+E(\varepsilon)+\tau\}},\qquad
 E(\varepsilon)=3\Omega(\varepsilon)-2\log(1-\varepsilon)
                         \longrightarrow0 .
 \tag{27}
\]
The unselected second sector needs only one logarithmic term;
(27) deliberately retains the larger common bound for both.

## 5. Calibration and continuous seam pieces

The [three-factor affine-floor theorem](research_mixed_complete44_three_factor_affine_floor.md)
proves, on exactly (1),
\[
             \Lambda_{123}(z)+\frac\beta2\Re g(z)>\frac73.
 \tag{28}
\]
It is a lower bound for the original action and its affine
marginal, obtained from eligible formal profile trials. It is
not a lower bound for any finite cap, kernel, or signed sum.

The remaining scalar comparison after (28) is rational:
\[
\begin{split}
 B_{44}
 &<\frac{433}{500}+\frac{39}{80}+\frac7{15}
      =\frac{10921}{6000},\\
 m_1&<m_0,\qquad
 B_{44}+m_\beta<
       \frac{69857}{30000}
       =\frac73-\frac{143}{30000},\qquad
 \frac{143}{30000}>\frac1{250}.
\end{split}
 \tag{29}
\]
For \(\beta=1\), the actual third plateau has negative height.
The absolute Fourier bound therefore supplies
\[
 D_{1,N}(Z)\le C_\tau N^{B_\tau}
                         e^{N\{-\Re g(z)/2+\tau\}}.
 \tag{30}
\]
Here \(\Re g(z)<0\) on \(0<\Re z<1/2,\Im z<0\), so the
factorial alternative dominates the zero forced rate. No
nonvanishing or division is needed. For \(\beta=0\), (30)
is replaced by the identity \(D_{0,N}=1\).

Choose a fixed collar radius \(\varepsilon>0\) so small that
\(E(2\varepsilon)<1/1000\), with \(2\varepsilon<1\).
Allocate a total rate tolerance below \(1/1000\) to all finite
source estimates, the ordinary-color neighborhood, and (30).
Equations (27)--(30) then give, on the larger collar,
\[
 |\mathscr D_{\sigma,\beta,N}(w,Y,Z)|D_{\beta,N}(Z)
       \le C N^B e^{N\{\Lambda_{123}(z)-1/500\}},
              \qquad |Y-1|\le2\varepsilon .
 \tag{31}
\]
Indeed \(1/1000+1/1000+1/500=1/250<143/30000\).
This bound holds for both parities and all real ordinary colors,
and on a sufficiently small fixed complex neighborhood of the
complete color. The common choices precede \(N\).

For every fixed number of \(Y\) and ordinary-color derivatives,
Cauchy's formula gives the same rate on \(\mathcal V_\varepsilon\)
and smaller color disks. At a fixed outgoing \(Z\), the multiplier
(6) is constant in those variables, even when it is zero. It is
neither differentiated nor divided out.

The logarithmic preimage of \(\mathcal V_\varepsilon\) contains
fixed complex neighborhoods of \(y=0\) and \(y=1\). Thus (31)
pays short real second-coordinate arcs at both ends, and any
fixed finite-length joins contained in those neighborhoods.
Integrating with the original \(N\,dy\) changes only the
polynomial prefactor. The first \(N\) has already been retained
in (22); no further scalar, Gram adapter, or physical sampling
factor is introduced.

The collar is not asserted to reach height \(c_2\), the selected
height \(1/100\), or the old second plateau. The remaining second
arcs and their connections must still be estimated. Nor does
(31) assert cancellation or a nonzero leading coefficient for
the complete next transfer. Its source is the entire first
polynomial (4), rather than a restricted or local first message.

## Direct source versions

The following directly used source implications have been read and
their versions checked.

* Pointwise prefix replacement: literal \(f_{44}\), its first
  coefficient, physical normalization, and ordinary-color degree.
* Terminal real-color decay, Lemma 2, and cap seam source, Theorem 1:
  the complete coherent norm (10), including both actual endpoint
  groups, real colors and fixed complex-color neighborhoods.
* Complete next-source seam collar, Sections 1--2: the exact
  inequalities (16)--(18), uniform factorial estimates and
  \(c_{\rm b}<13/40\).
* Next first physical end, Section 1, equation (4): the literal
  finite binomial identity used in (11). No physical terminating
  support from that source is imposed here.
* Transformed real-initial interval, equations (13)--(15): the
  full disk numerator sum (20).
* Low-index kernel margin, Section 2: the all-row disk estimates
  (24)--(25), with both typed output radii.
* Fourier-weight continuation: cardinal identity (14), the
  outgoing absolute halfweight and its negative-height sign.
* Second-selected plateau reduction: actual reference domains,
  third ordinary incidence, and original allocations and action.
* Three-factor affine floor, complete proof: (28), with the same
  original action and the outgoing halfweight on the stated side.

| Source | SHA-256 |
|---|---|
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |
| research_mixed_terminal_real_color_decay.md | 902a9a7aca0991fe80fbefbd4a703932a1d04c46b31db1f4c8e42d7d71330a6f |
| research_mixed_cap_seam_source_bounds.md | 88e07855c29788902c79ba9727f633a213e8fea5a0cc224092725b2e706dc75d |
| research_mixed_next_complete_source_seam_collar.md | 36e99887181637d8a41cd072f1d382560c838ad70029ab1b89ae7216b50bc970 |
| research_mixed_three_four_next_first_physical_end.md | dc3160221705876603dfaae3f005b6fa1a993768214e61407d19b7057d6d4f61 |
| research_mixed_transformed_real_initial_interval.md | c6b2ae80f47dfcc113a823f8c883fed54c7c1d06d6dfb8ed945bbb16744bcc9c |
| research_mixed_next_low_index_kernel_margin.md | 35de8662e57070a4f19aef409f82c921283493ba3f0e17268f1c11a7eac1738c |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_second_selected_plateau_reduction.md | 015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f |
| research_mixed_complete44_three_factor_affine_floor.md | 112f3b5a8d40c7a3bb770b8deae7b189c4729235851d8a2036f8869edc332b7d |

Author full proof readback and all ten direct-source implication
reads and hash checks are complete.
Independent full proof and direct-source review is required before
adoption. All work is written finite-source and analytic reasoning. No
mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation, or frozen-source change is used.
