# A complete next-source bound on a fixed period-seam collar

Research deduction, 8 November 2026. A fixed complex neighborhood of
the second-coordinate seam is exponentially small for the original
next-four source, in either Fourier sector. The same argument covers
the terminal-three reference and ordinary-next-three references whose
output has nonpositive height. Every finite row and the whole
transformed prefix are retained. This is a bound on continuous
contour pieces, not just a deletion of physical nodes.

The collar width is fixed but not specified. In particular it is not
asserted to reach the selected height \(1/100\). The estimate is local
in the actual next-output references; it is not an affine comparison
on an independent outgoing plateau. No numerical evaluation is used.

## 1. Literal source and a small seam factor

Write \(D=N-1\), \(r=e^{-2\pi i/N}\),
\(P_j=(r;r)_j\), \(S_j=|P_j|\), and \(p_j(X)=(rX;r)_j\).
Keep
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{e=0}^{D}
              H_N(w,r^{-e})\,p_e(X)/P_e,\\
 C_{\beta,N}(X,Z)&=\sum_{j=0}^{D}
              X^{-j}p_j(X)p_j(Z)/P_j^{2+\beta},\\
 F_N(w,Y)&=F_{34,N}(w,Y)
       =N\operatorname{CT}_X[U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 D_{\sigma,\beta,N}(w,Y,Z)
       &=F_N(w,Y)d_N(Y)Y^{-\sigma N}C_{\beta,N}(Y,Z),
       \qquad \sigma=0,1.
\end{split}
\tag{1}
\]
The complete transfer is \(N[Y^0](F_Nd_NC_\beta)+
N[Y^N](F_Nd_NC_\beta)\). Thus both values of \(\sigma\) in
(1) occur for either next letter. There is no additional Gram
factor or root-average multiplier.
At a physical output \(Z=r^k\), the original next row is restored
by the unchanged scalar
\(\kappa_N^{4+\beta}N^{1+\beta}P_k^{1-\beta}\), as in
[the exact attachment identity](research_mixed_three_four_next_conditional_attachment.md).
The estimates here concern precisely the conditional source before
that restoration.

For \(0<\varepsilon<1\) let
\[
 \mathcal V_\varepsilon=\{Y:|Y-1|\le\varepsilon\}.
 \tag{2}
\]
This is a fixed neighborhood of \(Y=1\); its additive logarithmic
preimage has periodic copies at \(y=0,1\). Put
\[
 \Omega(\varepsilon)=
 \log(1+\varepsilon/2)
       +\frac{\varepsilon}{2}\log(1+2/\varepsilon),
 \qquad J(t)=\int_0^t\log(2\sin\pi s)\,ds .
 \tag{3}
\]
There is an exact finite product bound
\[
 \frac{|p_j(Y)|}{S_j}\le e^{N\Omega(\varepsilon)},
 \qquad 0\le j<N,\quad Y\in\mathcal V_\varepsilon .
 \tag{4}
\]
Indeed each ratio of factors is at most
\(1+\varepsilon/|1-r^k|\). For \(1\le k<N\), concavity of sine
gives \(|1-r^k|\ge4\min(k/N,1-k/N)\). Pair \(k\) with \(N-k\)
and use the decreasing function
\(f(t)=\log(1+\varepsilon/(4t))\). The logarithm of the product
of these bounds over the full period is at most
\[
 2\sum_{k=1}^{\lfloor N/2\rfloor}f(k/N)
 \le 2N\int_0^{1/2}f(t)\,dt=N\Omega(\varepsilon).
 \tag{5}
\]
For even \(N\), the sum on the left harmlessly counts the middle
factor twice. For odd \(N\), it pairs every factor once.
The first inequality also holds for any shorter prefix product,
since every factor in this positive majorant is at least one.
This proves (4) at every level, including all numerator zeros.
In particular \(\Omega(\varepsilon)\to0\) as \(\varepsilon\downarrow0\).

The exact identity
\[
       d_N(Y)=\frac1N C_{0,N}(1,Y)
             =\frac1N\sum_{j=0}^{D}\frac{p_j(Y)}{P_j}
 \tag{6}
\]
is [the first-node identity, Lemma 1](research_mixed_next_three_first_physical_node.md).
It holds as an identity of entire polynomials, not merely on the
root grid. Hence (4) gives an arbitrarily small exponential rate
for the complete \(d_N\) on (2). Its polynomial forcing has not
been discarded. Also
\[
 |Y^{-j}|,\ |Y^{-\sigma N}|
                 \le e^{-N\log(1-\varepsilon)} .
 \tag{7}
\]
All these costs tend to zero with \(\varepsilon\). Below,
\(\tau>0\) denotes an arbitrarily small total tolerance in the
previously proved global coefficient and disk estimates.

## 2. A rational sine-factorial bound

Put \(c_{\rm b}=-2J(1/6)\). We shall use the strict elementary bound
\[
                         c_{\rm b}<\frac{13}{40}.
 \tag{8}
\]
For \(0<s\le1/6\), the sine cubic lower bound gives
\[
 \log(2\sin\pi s)
 \ge \log(2\pi s)+\log(1-\pi^2s^2/6)
 \ge \log(2\pi s)-\frac{\pi^2s^2}{6(1-\pi^2/216)}.
\]
Use \(\pi^2<10\), \(\pi>157/50\), and
\(\log(157/150)>14/307\), the last following from
\(\log t\ge2(t-1)/(t+1)\), strictly for \(t>1\).
Integration yields
\[
 -J(1/6)<\frac{293}{1842}+\frac5{1854}<\frac{13}{80}.
 \tag{9}
\]
For the last comparison,
\(13/80-293/1842=253/73680\), and
\(253\cdot1854-5\cdot73680=100662>0\).
The elementary bounds for \(\pi\) may be taken from the written
Machin witness in
[the low-index kernel margin, equation (15)](research_mixed_next_low_index_kernel_margin.md);
its lower bound \(333/106\) is greater than \(157/50\).
This proves (8) without an evaluation.

## 3. Bound the complete prefix before the next attachment

The original coherent all-real-color norm is
\[
 \sum_{e=0}^{D}|H_N(w,r^{-e})|
       \le C_\tau N^B e^{N(b_0+\tau)},\qquad
                 b_0=\frac{101}{125},\quad w\in[-2,2].
 \tag{10}
\]
This is [terminal real-color decay, Lemma 2](research_mixed_terminal_real_color_decay.md);
the [cap seam source theorem](research_mixed_cap_seam_source_bounds.md)
gives its small fixed complex complete-color version.
The finite \(r\)-binomial formula gives, uniformly on \(|X|=1\),
\[
 \frac{|p_e(X)|}{S_e}
 \le \sum_{k=0}^{e}\frac1{S_kS_{e-k}}
 \le C_\tau N^B e^{N(c_{\rm b}+\tau)}.
 \tag{11}
\]
All denominator indices are less than \(N\). Equations (10)--(11)
bound the whole cap by the rate \(b_0+c_{\rm b}\). Each \(H_N\)
is kept coherent; its individual Newton terms are not substituted.

Let \(L(t)=-2J((1-t)/2)\), and set
\[
 M_\beta(C)=\max_{0\le t\le1}
        \{L(t)-(1+\beta)J(t)+Ct\}.
 \tag{12}
\]
The complete disk numerator bound and the scalar estimate
\[
  M_1(0)<\frac7{15},\qquad
  \sup_{|X|\le1}\sum_{j<N}\frac{|p_j(X)|}{S_j^2}
       \le C_\tau N^B e^{N(7/15+\tau)}
 \tag{13}
\]
are [the transformed initial-interval theorem, equations (13)--(15)](research_mixed_transformed_real_initial_interval.md).
On \(|X|=1\), (4) and (13) give
\[
 |C_{1,N}(X,Y)|
 \le C_{\tau}N^B
       e^{N\{7/15+\Omega(\varepsilon)+\tau\}}.
 \tag{14}
\]
Inserting (10)--(14) into the actual full-circle integral defining
\(F_N\), with its factor \(N\), proves
\[
 |F_N(w,Y)|\le C_{\tau}N^B
  e^{N\{b_0+c_{\rm b}+7/15+\Omega(\varepsilon)+\tau\}}.
 \tag{15}
\]
This is a bound for the complete prefix on a complex seam collar.
It is not inferred from its single value at \(Y=1\).

For the next kernel (4), (7), and the same disk estimate give
\[
 \sup_{|Z|\le R}|C_{\beta,N}(Y,Z)|
 \le C_{\tau}N^B
 e^{N\{M_\beta(\log_+R)+\Omega(\varepsilon)
                                  -\log(1-\varepsilon)+\tau\}}.
 \tag{16}
\]
Every incoming row remains, including all rows revived away from
the seam. Consequently, for either \(\sigma\),
\[
 \sup_{|Z|\le R}|D_{\sigma,\beta,N}(w,Y,Z)|
 \le C_{\tau}N^B
 e^{N\{b_0+c_{\rm b}+7/15+M_\beta(\log_+R)
                     +E(\varepsilon)+\tau\}},
 \qquad
 E(\varepsilon)=3\Omega(\varepsilon)-2\log(1-\varepsilon)
                    \longrightarrow0.
 \tag{17}
\]
The unselected density has only one of the two logarithmic costs;
(17) deliberately uses a common upper bound for both sectors.
This proof retains both Fourier alternatives through the exact
polynomial (6).

## 4. Actual action comparisons

Use the original conditional next action
\(\mathcal P_\beta^+\) and the matched ordinary or terminal
references of [the local next-source theorem](research_mixed_three_four_next_local_source.md).
No outgoing Gram incidence is added.
The written action floors in
[the low-index kernel margin, equation (23)](research_mixed_next_low_index_kernel_margin.md)
are
\[
 \begin{array}{c|c}
 \text{reference}&\Re\mathcal P_\beta^+(-2,z_*)\\ \hline
 \text{ordinary three}&>2+\chi\\
 \text{terminal three}&>52/25+\chi\\
 \text{ordinary four}&>199/100+2\chi\\
 \text{terminal four}&>41/20+2\chi
 \end{array},
 \qquad \chi=\frac{117}{800\pi}>\frac{819}{17600}>\frac9{200}.
 \tag{18}
\]
These are statements at the actual correlated output coordinates.

**Next four.** Every ordinary or terminal next-four output has
\(|Z_*|<1\). Taking \(R=1,\beta=1\) in (17) gives the limiting
ceiling
\[
 b_0+\frac{13}{40}+\frac{14}{15}
       =\frac{6199}{3000}
       <\frac{207}{100},\qquad
 \frac{207}{100}-\frac{6199}{3000}=\frac{11}{3000}.
 \tag{19}
\]
Both next-four action floors exceed \(207/100\).

**Next three with nonpositive output height.** On \(|Z_*|\le1\),
\(M_0(0)=c_{\rm b}\). Indeed
\((L-J)'=-\log(2\sin(\pi t/2))\), so its maximum is at
\(t=1/3\), with value \(-3J(1/3)=-2J(1/6)\) by sine
duplication. Thus the limiting ceiling is
\[
 b_0+\frac{13}{20}+\frac7{15}
              =\frac{2887}{1500}<2.
 \tag{20}
\]
This covers ordinary-next-three references subject to the stated
output-height restriction. It also covers such terminal references.

**All terminal-three outputs.** The whole typed output disk is
\(|Z|\le\exp(17\pi/125)\). On this disk the written bound
\(M_0(17\pi/125)<1271/2500\) from the same kernel-margin theorem
gives
\[
 b_0+\frac{13}{40}+\frac7{15}+\frac{1271}{2500}
       =\frac{31621}{15000}<\frac{211}{100}<\frac{17}{8}.
 \tag{21}
\]
The terminal-three floor in (18) is greater than \(17/8\).
No assertion is made for the full ordinary-next-three family at
positive output height: (21) alone does not pay its floor in (18).

**Theorem.** There is a fixed sufficiently small \(\varepsilon>0\) such
that, on each of the reference families just specified, both Fourier
densities (1) have an exponential gap relative to the original
conditional next action. This holds uniformly for all real ordinary
colors with the complete-color action as normalization, for both
level parities, and for every fixed ordinary-color derivative.
On fixed smaller complete-color and actual-output neighborhoods,
all fixed mixed derivatives of
\[
 e^{-N\mathcal P_\beta^+(w,z)}
      D_{\sigma,\beta,N}(w,e^{-2\pi iy},e^{-2\pi iz})
 \tag{22}
\]
are \(O(e^{-N/2000})\), after shrinking the common seam collar.

To prove the theorem, choose \(\varepsilon\) and the total tolerance in
(17) within the smallest strict reserve (19). Compactness and
holomorphy preserve a smaller reserve near the actual reference
families. If an output lies on \(|Z|=1\), enlarge the disk slightly:
\(M_\beta(C)\le M_\beta(0)+C\), so the strict reserve persists.
The all-real derivative assertion follows by Markov's inequality
for the full polynomial in \(w\). The original complex-color norm
and Cauchy's formula on smaller fixed neighborhoods prove (22).
The factor \(Y^{-\sigma N}\) is holomorphic on these collars and
is already included in (7); no modulus halfweight is differentiated.

At an ordinary output one may restore the usual
\(|d_N(Z)|^{\beta/2}\) allocation locally. For \(\beta=1\), its
nonzero factorial packet gives the exact action shift
\(-\Re g(z_*)/2\), matching the original following affine
normalization at \(z_*\). This local statement does not divide by
the halfweight on the independent outgoing plateau.

## 5. The older filtered prefix has the same collar bound

Keep exactly the older \(11/12\) filter of
[paired localization, Section 5](research_mixed_next_low_cardinal_paired_localization.md):
\[
 F_N^{\rm mid}=(I-\Pi_{\rm end})(F_N-R_N^a),\qquad
 E_N^{\rm all}=F_N-F_N^{\rm mid}.
 \tag{23}
\]
Here the first physical cutoff is \(\lceil23N/24\rceil\), the
upper second cutoff is \(\lceil11N/12\rceil\), and the lower
second cutoff is the fixed one in that theorem. Its equation (32)
proves, with all-real and small complex-color scopes retained,
\[
 \sup_{|Y|\le1}|E_N^{\rm all}(w,Y)|
                 \le CN^B e^{77N/50},\qquad
                      \deg_Y E_N^{\rm all}\le D.
 \tag{24}
\]
Thus on (2) polynomial degree costs at most
\(e^{N\log(1+\varepsilon)}\). Combining this with (4), (6),
(7), and (16) proves the correction-density bound with limiting
rate \(77/50+M_\beta(\log_+R)\), and extra rate at most
\[
 2\Omega(\varepsilon)+\log(1+\varepsilon)
                         -2\log(1-\varepsilon)\longrightarrow0.
 \tag{25}
\]
The three respective ceilings used in Section 4 are
\[
 \frac{77}{50}+\frac7{15}=\frac{301}{150}<\frac{207}{100},
 \qquad
 \frac{77}{50}+\frac{13}{40}=\frac{373}{200}<2,
 \qquad
 \frac{77}{50}+\frac{1271}{2500}
                         =\frac{5121}{2500}<\frac{17}{8}.
 \tag{26}
\]
Subtracting this complete correction proves the theorem, including
its fixed mixed derivatives, with \(F_N^{\rm mid}\) in place of
\(F_N\), on a smaller common collar. No separate coefficient
suppression is used in this pointwise argument.
This statement keeps the specified old filter; it does not assert
the \(77/50\) bound for the distinct later \(8/9\) filter.

## 6. Contour use and remaining scope

If a fixed incoming \(y\)-path is contained in (2), its contribution
with the original outer density \(+N\,dy\) has the same exponential
gap. This includes the continuous seam intervals at both ends of
a period, and short connectors contained in the proved collar.
Both \(N\)'s are retained: the first in the complete prefix (15),
the second in the next coefficient integral.

One may therefore choose a selected periodic contour that is real
near \(y=0,1\), rises elsewhere to the selected central plateau,
and descends again before its final seam interval. Periodicity and
the literal finite Laurent source justify that contour choice
exactly. The present theorem pays its seam pieces only. The
transitions from this collar to height \(1/100\), the other
second-coordinate complement, and the corresponding unselected
complement still require bounds or a valid paired estimate.
No physical-index deletion is identified with any of these arcs.
Nor does the estimate assert that a full half-grid side at the
original heights lies inside (2). A meromorphic paired-cycle
denominator such as \(1-Y^N\) must still be treated with its
actual residues or half-grid bounds before using this density
estimate on a corresponding current.

The ordinary and terminal scopes in Section 4 are separate source
claims. This collar estimate supplies no whole next-transfer
asymptotic and no new short-filling knot theorem.
