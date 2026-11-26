# The actual long-transfer cross-collar kernel

Private written proof, 18 November 2026.

The opposite endpoint blocks excluded from the short Euler transition
have an exact finite kernel with a genuine factor \(N\).
This note gives both signed factors, their checked-crossing order,
their endpoint gauges, and their finite Fourier kernels. The root
reflection identity is used only after specialization. The full
unreflected products are retained for every quantum/meridian normal.

The sole complete direct E supplies the literal balanced matrices,
crossing order, gauges and two-wall convention. All new reflection,
phase and Fourier calculations are given below. No neighboring packet,
contributing cycle or scalar noncancellation is assumed.

## 1. The full finite germ before reflection

Fix \(N\ge2\), \(d=N-1\), and write
\[
 Q=e^h,\qquad q=e^{h/2},\qquad x=-M/q,\qquad
 F_t=\prod_{j=1}^t(1-Q^j),\quad
 H_t=\prod_{j=1}^t(MQ^{-j}-M^{-1}).
 \tag{1}
\]
Empty products equal one. E's compressed arrows are
\[
 {\cal E}|a\rangle=(MQ^{-a}-M^{-1})|a-1\rangle,\qquad
 F|b\rangle=(1-Q^{b+1})|b+1\rangle
 \tag{2}
\]
away from their forced extremes; \({\cal E}|0\rangle=F|d\rangle=0\).
Put \(A={\cal E}\otimes F\), and
\[
 \Theta^\pm
   =\sum_{n=0}^d\frac{\sigma_n^\pm}{F_n}A^n,\qquad
 \sigma_n^+=(-1)^nq^{n^2},\qquad \sigma_n^-=q^n.
 \tag{3}
\]
Here \(\Theta^-=(\Theta^+)^{-1}\). The actual crossings are
\[
 R^+=\kappa\,{\mathsf P}D\Theta^+,\qquad
 R^-=\kappa^{-1}\Theta^-D^{-1}{\mathsf P},\qquad
 D_{a,b}=x^{-a-b}Q^{ab}.
 \tag{4}
\]
The original scalar Cartan line \(\kappa\), all pivots, and every
neighboring tensor are unchanged.

Take nonnegative endpoint deficits \(u,v,w,z\) satisfying
\[
 s=u+w=v+z\le d,\qquad n=d-s.
 \tag{5}
\]
The uncheck block goes from
\((a,b)=(d-u,v)\) to \((w,d-z)\).
This is an actual transfer of length \(n\); it has not been replaced
by a short transfer modulo \(N\). Direct multiplication of (2) gives
\[
 T^\pm_{u,v;w,z}
 :=(\Theta^\pm)_{(w,d-z),(d-u,v)}
 =\frac{\sigma_n^\pm}{F_n}
       \frac{H_{d-u}}{H_w}\frac{F_{d-z}}{F_v}.
 \tag{6}
\]
The head support and conservation condition (5) are part of this
formula. Every index in a denominator lies below \(N\).

For an exact form adapted to normals define
\[
 U_F(t)=\prod_{r=1}^t(1-Q^{N-r}),\qquad
 U_H(t)=\prod_{r=1}^t(MQ^{r-N}-M^{-1}).
 \tag{7}
\]
Thus \(F_{d-t}=F_d/U_F(t)\) and \(H_{d-t}=H_d/U_H(t)\)
where these factors are units. In E's normal bidisk they are units.
Canceling only the identical full factor \(F_d\) gives
\[
 \boxed{\quad
 T^\pm_{u,v;w,z}
 =\sigma_n^\pm H_d
       \frac{U_F(s)}{U_H(u)F_vH_wU_F(z)} .
 \quad} \tag{8}
\]
This is an identity of the unspecialized finite analytic germ,
not a derivative of a root reflection.

Let \(T=d-u+v=w+d-z\). The two checked blocks, in their different
physical input orders, are exactly
\[
 R^+_{(d-z,w),(d-u,v)}
       =\kappa x^{-T}Q^{w(d-z)}T^+_{u,v;w,z},
 \tag{9}
\]
\[
 R^-_{(w,d-z),(v,d-u)}
       =\kappa^{-1}x^TQ^{-(d-u)v}T^-_{u,v;w,z}.
 \tag{10}
\]
The inverse Cartan factor acts on the input after the flip.
It cannot be put on the positive crossing's output.

## 2. Reflection at the complete root and all signed phases

For the root formulas below, specialize
\[
 h=2\pi i/N,\qquad M=1,\qquad Q^N=1,\qquad q^N=-1.
 \tag{11}
\]
For \(0\le t\le d\), factor \(X^N-1\) and then reverse the last
\(t\) factors of \(F_d\). This proves
\[
 F_d=N,\qquad
 \frac{F_d}{F_{d-t}}
   =\prod_{r=1}^t(1-Q^{-r})
   =(-1)^tQ^{-t(t+1)/2}F_t,
\qquad
 F_{d-t}=\frac{N(-1)^tq^{t(t+1)}}{F_t}.
 \tag{12}
\]
Also \(H_j=Q^{-j(j+1)/2}F_j\). The unreflected coefficient
can therefore first be written
\[
 T^+_{u,v;w,z}
  =(-1)^nq^{-n(2w+1)}
                   \frac{F_{d-u}F_{d-z}}{F_{d-s}F_wF_v},
 \tag{13}
\]
\[
 T^-_{u,v;w,z}
  =q^{-n^2-2nw}
                   \frac{F_{d-u}F_{d-z}}{F_{d-s}F_wF_v}.
 \tag{14}
\]
For example, the exponent in (13) comes from
\(q^{n^2}Q^{-n(d-u)+n(n-1)/2}\) and \(d-u=n+w\).
Substitution of (12) gives the common factorial core
\[
 {\cal C}_{u,v;w,z}
       =N\frac{F_s}{F_uF_vF_wF_z}
 \tag{15}
\]
and the phases
\[
 T^+_{u,v;w,z}
 =(-1)^{N+u+z}q^{(w+1)^2+u+z(z+1)}
                                {\cal C}_{u,v;w,z},
 \tag{16}
\]
\[
 T^-_{u,v;w,z}
 =(-1)^{u+z-s}
   q^{-n^2-2nw+u(u+1)+z(z+1)-s(s+1)}
                                {\cal C}_{u,v;w,z}.
 \tag{17}
\]
In (16), reducing \(q^{-2dw}\) uses \(Q^d=Q^{-1}\), and
\(q^{-d}=-q\). These reductions are root identities.

Keeping the full \(D,{\mathsf P}\) factors in (9)--(10) yields
particularly simple balanced checked entries:
\[
 \boxed{\quad
 R^+_{(d-z,w),(d-u,v)}
   =\kappa(-1)^s q^{s+(u-v)^2}{\cal C}_{u,v;w,z},
 \qquad
 R^-_{(w,d-z),(v,d-u)}
   =\kappa^{-1}q^{(u-z)^2}{\cal C}_{u,v;w,z}.
 \quad} \tag{18}
\]
These follow by multiplying (13) or (14) by the displayed
Cartan factor before reducing powers. In particular,
\[
 T^+_{0,0;0,0}=Nq^{d^2}=(-1)^NNq,\qquad
 T^-_{0,0;0,0}=(-1)^dNq^d=(-1)^NNq^{-1},
 \tag{19}
\]
\[
 R^+_{(d,0),(d,0)}=N\kappa,\qquad
 R^-_{(0,d),(0,d)}=N\kappa^{-1}.
 \tag{20}
\]
For \(N\ge2\), \(R^-_{(d,0),(d,0)}=0\): the flip gives input
\((0,d)\) to the inverse Euler factor, which can only have transfer
zero. The large inverse corner in (20) is the opposite physical
corner. The same observation gives \(R^+_{(0,d),(0,d)}=0\).

## 3. Exact endpoint gauges and the symmetric kernel

Use E's \(G_F|a\rangle=F_a|a\rangle\). On both heads,
the uncheck transformed entry is the original one multiplied by
\(F_{d-u}F_v/(F_wF_{d-z})\). Before specialization it is
\[
 (T^\pm)_{FF}
   =\sigma_n^\pm\frac{H_{d-u}F_{d-u}}{H_wF_wF_{d-s}}
   =\sigma_n^\pm H_d
        \frac{U_F(s)}{U_H(u)U_F(u)H_wF_w}.
 \tag{21}
\]
At the root it depends on \(u,w\) alone, apart from conservation:
\[
 B_N^+(u,w)=(-1)^NNq^{u^2+w^2+2s+1}
                                  \frac{F_s}{F_u^2F_w^2},
 \tag{22}
\]
\[
 B_N^-(u,w)=(-1)^{N+s}Nq^{-1-s-2uw}
                                  \frac{F_s}{F_u^2F_w^2}.
 \tag{23}
\]
For instance the positive unreduced exponent is
\(-n(2w+1)+2u(u+1)-s(s+1)\); (22) follows using
\(n=d-s\). This also verifies the input/output gauge order.

For the other physical endpoint chart,
\(G_E|a\rangle=H_a^{-1}|a\rangle\), the exact expression is
\[
 (T^\pm)_{EE}
   =\sigma_n^\pm H_d
        \frac{U_F(s)}{U_H(z)U_F(z)H_vF_v}.
 \tag{24}
\]
Its root value is \(B_N^\pm(z,v)\).
Thus both separated endpoint types have the same scalar kernel
with their appropriate deficit pair.

Write \(S_t=\prod_{j=1}^t2\sin(\pi j/N)\). Since
\(F_t=(-i)^tq^{t(t+1)/2}S_t\), equations (22)--(23) become
\[
 B_N^\pm(u,w)=(-1)^NN\,(\pm i)^s
       q^{\pm(s+1)(s+2)/2}
                       \frac{S_s}{S_u^2S_w^2}.
 \tag{25}
\]
Here the upper sign is positive Euler; the lower sign is its inverse.
The two kernels are entrywise complex conjugates at the root and
are symmetric in \(u,w\). This is not a positivity assertion about
the full crossing or its contraction.

One can also display a Gaussian-binomial core without discarding
any source factor. Multiply an input upper-donor column with deficit
\(u\) by \(F_u\), and an output lower-donor row with index \(w\)
by \(F_w\). Equivalently apply an additional diagonal change with
value \(F_u\) on the upper collar and \(F_w^{-1}\) on the lower
collar. For disjoint collars this is one well-defined head gauge.
The resulting block is exactly
\[
 \widetilde B_N^\pm(u,w)=F_uF_w B_N^\pm(u,w),
 \tag{26}
\]
with core \(N F_{u+w}/(F_uF_w)\) and the phases (22)--(23).
All neighboring rows and columns carry the inverse changes.
On the donor, combining this change with \(G_F\) gives lower
value one and upper value
\(F_{d-u}F_u=N(-1)^uq^{u(u+1)}\) at the root.
For \(EE\), multiply the lower-recipient input column by \(F_v\)
and the upper-recipient output row by \(F_z\).

For widths \(R=o(N)\), these are source changes with
subexponential condition numbers. Indeed for \(t\le R<N/2\),
\[
 (4/N)^t t!\le |F_t|\le (2\pi/N)^t t!.
 \tag{27}
\]
The lower factorials and their reciprocals have maximum
\(\exp(O(R\log(eN/R)))\); (12) gives the same upper-collar
bound with an additional factor \(N\). Set the diagonal change
to one outside the selected collars. Every entry of the selected
block is still transformed by its exact input/output values.
This does not compress away the path through the bulk or invoke
the short-interval identity \(PA^nP=(PAP)^n\) on a union of collars.

There is a uniform Pascal-core limit on the \(\sqrt N\) deficit scale.
Replacing \(F_u,F_w\) in the compensated root rescaling by their
positive moduli \(S_u,S_w\) gives the exact kernel
\[
 S_uS_w B_N^\pm(u,w)
   =(-1)^NN(\pm i)^s q^{\pm(s+1)(s+2)/2}
                                      \frac{S_s}{S_uS_w}.
 \tag{27a}
\]
For \(s=u+w\le C\sqrt N\),
\[
 \frac{S_s}{S_uS_w}
       =\binom{s}{u}\bigl(1+O_C(N^{-1/2})\bigr).
 \tag{27b}
\]
Indeed
\(S_t=(2\pi/N)^t t!\exp E_t\), where
\[
 |E_t|
 =\left|\sum_{j=1}^t\log\frac{\sin(\pi j/N)}{\pi j/N}\right|
 \le C_1t^3/N^2
\]
on this range. Apply this to \(t=s,u,w\); the powers of
\(2\pi/N\) cancel. The phase in (27a), including its quadratic
part, is retained. The elementary moment identity
\(\binom{u+w}{u}=(u!w!)^{-1}\int_0^\infty t^{u+w}e^{-t}\,dt\)
describes this factorial core only. The original crossing phases,
neighboring factors and closing functional are not positive by
this identity. The \(S\)-rescaling is a root statement. If its
analytic normal extension is desired, use
\(i^tq^{-t(t+1)/2}F_t\), which equals \(S_t\) at the root,
together with the unreflected formulas; do not differentiate
absolute values or the root reflection identity.

## 4. The finite Fourier kernel retains both ends

Take nonempty deficit intervals \(I_u,I_v,I_w,I_z\subset[0,R]\), with
their endpoints retained and \(s=u+w\le d\). For each \(s\), set
\[
 L(s)=\max(\min I_v,s-\max I_z),\qquad
 U(s)=\min(\max I_v,s-\min I_z),\qquad
 K_j(t)=\sum_{a=0}^j t^a .
 \tag{28}
\]
If \(L(s)>U(s)\), the corresponding term is zero. Otherwise
\[
 \sum_{\substack{v\in I_v\\s-v\in I_z}}t^v
                         =t^{L(s)}K_{U(s)-L(s)}(t).
 \tag{29}
\]
There is no denominator \(1-t\); at \(t=1\) the factor is
\(U(s)-L(s)+1\).

Use the root Fourier basis
\(|k\rangle_{\!F}=N^{-1/2}\sum_{a=0}^dQ^{ak}|a\rangle\).
Let \(j_1,j_2\) label the output Fourier heads and \(k_1,k_2\)
the input. The projected uncheck \(FF\) block is exactly
\[
 \frac{Q^{d(k_1-j_2)}}{N^2}
 \sum_{\substack{u\in I_u,\ w\in I_w\\u+w\le d}}
 B_N^\pm(u,w)
 Q^{(j_2-k_1)u+(j_2-j_1)w}
 t^{L(s)}K_{U(s)-L(s)}(t),\qquad t=Q^{k_2-j_2}.
 \tag{30}
\]
To check all Fourier signs before summing \(v\), its exponent is
\[
 k_1(d-u)+k_2v-j_1w-j_2(d-z)
 =d(k_1-j_2)+(j_2-k_1)u+(j_2-j_1)w+(k_2-j_2)v.
 \tag{31}
\]
This proves (30) with the exact upper-collar monomial.
For the balanced or \(EE\) block one may always use the same
four-index sum with its entry (16)--(17) or (24); this retains
the same conservation and interval masks without cancellation.

The checked \(FF\) kernels also have a finite geometric inner sum.
At the root, the positive one is
\[
 \frac{\kappa Q^{d(k_1-j_1)}}{N^2}
 \sum_{u,w}
 B_N^+(u,w)Q^{(j_1-k_1)u+(j_1-j_2)w}
 x^{u-d}Q^{w(d-s)}
 t_+^{L(s)}K_{U(s)-L(s)}(t_+),
 \quad t_+=x^{-1}Q^{w+k_2-j_1}.
 \tag{32}
\]
The inverse, with its physical input order from (10), is
\[
 \frac{\kappa^{-1}Q^{d(k_2-j_2)}}{N^2}
 \sum_{u,w}
 B_N^-(u,w)Q^{(j_2-k_2)u+(j_2-j_1)w}
 x^{d-u}
 t_-^{L(s)}K_{U(s)-L(s)}(t_-),
 \quad t_-=xQ^{u-d+k_1-j_2}.
 \tag{33}
\]
Both sums have exactly the ranges in (30). For (32), write
\(D_{w,d-z}=x^{u-d}Q^{w(d-s)}(x^{-1}Q^w)^v\).
For (33), write
\(D_{d-u,v}^{-1}=x^{d-u}(xQ^{u-d})^v\).
These identities prove the Cartan ordering in the Fourier formulas.

A prescribed mark depending on \(v\) stays inside the inner finite
sum; it is not replaced by the unmarked \(K\) in (29).
Likewise every further intermediate projector remains its actual
path mask or finite Fourier kernel. Equations (30)--(33) describe
the local bare crossing block, to be paired with the unchanged,
inversely transformed neighboring source. They are not a delta
approximation or an independent replacement of that source.

## 5. Full normal rows and the scope of the \(N\) corner

For the extreme corner, (8)--(10) give before specialization
\[
 R^+_{(d,0),(d,0)}
        =\kappa M^{-d}q^{Nd}H_d,\qquad
 R^-_{(0,d),(0,d)}
        =\kappa^{-1}(-1)^dM^dH_d .
 \tag{34}
\]
At root \(q\), with \(M\) still unspecialized, the whole polynomial
identity is
\[
 H_d=(-1)^dM^{-d}\sum_{r=0}^dM^{2r},\qquad
 {\cal D}_N(M)=M^{-d}\sum_{r=0}^dM^{2r}.
 \tag{35}
\]
Thus the two corners are
\(\kappa M^{-d}{\cal D}_N(M)\) and
\(\kappa^{-1}M^d{\cal D}_N(M)\).
The removable expression
\({\cal D}_N(M)=(M^N-M^{-N})/(M-M^{-1})\)
is shorthand for the whole sum, including at \(M=1\).
It is not replaced by \(N\) before taking meridian derivatives.

For genuine \(h\)-normals use (8)--(10), (21), and (24), not
(12), (16)--(18), or (25). In E's bidisk
\(|h-2\pi i/N|\le\eta N^{-2}\), \(|M-1|\le\eta N^{-1}\),
all displayed factors of indices below \(N\) are units.
The actual top rows
\[
 \delta=1-Q^N,\qquad w_{\rm top}=MQ^{-N}-M^{-1},\qquad
 [F,P_H]=\delta U,\quad[{\cal E},P_H]=-w_{\rm top}L
 \tag{36}
\]
and their mixed defect remain exactly as in E, with all gauge
factors conjugated before differentiation. Fixed root Fourier
bases may be kept for these germs; a varying Fourier transform,
if used instead, must itself be differentiated.

On the ordinary head path \(M=-q^N\), exactly
\[
 H_d=(-1)^d M^{-d}F_d.
 \tag{37}
\]
This follows from
\(MQ^{-j}-M^{-1}=-M^{-1}(1-Q^{N-j})\).
It does not identify an auxiliary ADO-pivot closed normal with an
ordinary colored-Jones normal: the full original pivot/twist
adapter remains necessary. No new uniform normal asymptotic is
asserted here.

The displayed \(N\) is therefore a literal local degree factor in
the original signed crossing, with its common scalar line retained.
It is distinct from a closing-current prefactor and is not counted
twice. The endpoint windows and neighboring contractions may still
annihilate a contribution. Nothing here proves a nonempty global
support sector, its occurrence in the original relative cycle, or
a lower bound for the knot scalar.

## Complete proof-source pin

* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.

The complete direct was freshly read nontruncated in the active
author sequence and every used implication checked. The earlier
endpoint-current note was searched for coverage: it retains the
opposite-collar blocks but does not evaluate this kernel.
Only written mathematics and source/text operations were used.
Frozen and public files are unchanged.
