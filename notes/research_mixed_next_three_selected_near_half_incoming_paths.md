# The noncentral incoming horizontals and taper near the selected half-period

Private finite-source proof, 8 November 2026. The complete initial
incoming segment, its taper, and the right incoming horizontal are
paid on the full selected shared interval \([9/20,1/2]+i/100\).
This is an extension of their source proofs, not an inference from
a bound on a single vertical side or its shrinking grid correction.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Actual source and statement

Keep the actual complete words in powers three and four beginning
\(343\), of length \(m\ge5\), their original reference
\((a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3)\), and the affine
rate \(\Lambda_{123}(z)\). Write
\[
\begin{gathered}
h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_t=\Im t_*,
\quad h_z=\Im z_*,\quad H=1/100,\\
-.072<h_a<0,\quad -.102<h_s<-.001,\quad
-.03<h_t,h_z<.02,\\
y=q+iH,\quad 9/20\le q\le1/2,\qquad
z=u+ih_z,\quad 3/10\le u\le39/100 .
\end{gathered}                                                     \tag{1}
\]
Every height belongs to the same actual reference. The following
own-three factor has no outgoing halfweight.

For \(D=N-1,\ r=e^{-2\pi i/N}\), retain
\[
\begin{gathered}
P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j,\qquad
C_{\beta,N}(V,W)=
\sum_{j=0}^{D}\frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}},\\
X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\qquad
\mathcal D_N(a;y,z,w)=
U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z).
\end{gathered}                                                     \tag{2}
\]
Here the cap is complete and coherent; \(d_N\) is the full forced
polynomial, with \(d_N(r^b)=P_b^{-1}\), of degree at most \(D\).

The original increasing incoming paths are
\[
\begin{split}
\Gamma_{\rm in}&=[0,1/10],\\
\Gamma_{\rm tap}&:\ a=x-i\lambda(x-1/10),\
 1/10\le x\le11/50,\quad \lambda=-h_a/(3/25),\\
\Gamma_H&=[9/20+ih_a,1/2+ih_a].
\end{split}                                                       \tag{3}
\]

**Theorem.** Uniformly on (1), all real ordinary colors
\(w\in[-2,2]\), both parities and all sufficiently large levels,
\[
|\mathcal D_N(a;y,z,w)|
 \le CN^B e^{N\{\Lambda_{123}(z)-1/10000\}},
\qquad a\in\Gamma_{\rm in}\cup\Gamma_{\rm tap}\cup\Gamma_H .
\tag{4}
\]
Each original \(+N\int_\Gamma\mathcal D_N\,da\) separately has
the same exponential bound with polynomial cost.
If
\[
F_N^\Gamma(w,Y)=N\int_\Gamma U_{0,N}(w,X)C_{1,N}(X,Y)\,da,
\qquad
K_N^\Gamma(y)=\frac{N F_N^\Gamma d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},
\tag{5}
\]
then the same rate bounds \(K_N^\Gamma\) pointwise and its
integral over any subinterval of (1), in either orientation.
No incoming-corner or outside-parameter jet conclusion is made.

## 2. Endpoint calibrations and the complete next source

Use the original bare phases
\[
Q_\beta(v;b,d)=g(b+v)+g(d+v)-(2+\beta)g(v)
                         -g(b)-g(d)+2\pi ibv,
\quad g'(\zeta)=\operatorname{Log}(1-e^{-2\pi i\zeta}).
\tag{6}
\]
The next controlling profiles are its main at height \(h_t\),
\(3/20\le v\le1/2\), the real cuts \(3/20,1/2\), and its
complete last rate \(L_0=2\pi(h_z)_+\). The two selected
weight rates remain separately
\[
W_{\rm fac}(y)=-\Re g(y)-2\pi H,\qquad W_{\rm force}(y)=0 .
\tag{7}
\]

At the endpoint \(a_0=11/50+ih_a\),
[near-half central, Theorem 1](research_mixed_next_three_selected_near_half_central.md)
proves, at every \(q\) in (1),
\[
B_U(11/50)+\phi_1(a_0,y)+\phi_0(y,z)+W_\nu(y)
 <\Lambda_{123}(z)-1/400+1/1560
 <\Lambda_{123}(z)-1/1000 .                                  \tag{8}
\]
The first profiles here are every main index
\(1/8\le s_R\le1/2\) at \(h_s\), the two real cuts, and
the full first last rate \(-2\pi h_a+2\pi H\).
The estimate is profilewise before summation.

For \(a\in\Gamma_H\), Sections 3--4 of
[the right half-grid proof](research_mixed_next_three_half_grid_incoming_right_horizontal.md)
establish the same upper-endpoint comparison (8), with \(B_U(x)\),
for every first main \(1/20\le s_R\le1/2\) at \(h_s\) and its
real half profile. Although its equation (21) is recorded at
\(q=1/2\), its proof gives the assertion on every
\(9/20\le q\le1/2\): the original \(q=9/20\) reserve is at
least \(1/400\); both joint nonlast derivatives are negative;
the only next-last increase is bounded on every subinterval by
\((1/40)\log(40/39)<1/1560\). Thus no interpolation from a
single shared endpoint is being used.

Raw groups use
[half-grid bounded factor, Theorem 1(1)](research_mixed_next_three_half_grid_bounded_prefix.md).
Any index-independent preceding envelope of rate at most
\[
B_f=77/50+\pi/50
\tag{9}
\]
is paid against the complete \(d_N(Y)Y^{-N}C_{0,N}(Y,Z)\) on
the whole interval (1), with gap \(1/1000\).
This theorem includes every next physical row, alias and
unweighted join. It needs no division by a preceding factor.

For the nonraw groups use the explicit complete next reduction
in Sections 3--6 of near-half central: real cuts \(3/20,1/2\),
main height \(h_t\), aliases \(-1/5,+8\), four weighted sides
and both unweighted joins. Its next argument bounds
\(-39\pi/50\le\Im Q_{0,t}\le11\pi/10\) hold at every height.
The low block increases to its real cut; the whole upper
physical block reduces positively to half or last by
transformed-upper-row Lemma 1 on its full square.
These same-coordinate reductions retain each attached first
profile. They do not split an estimate for a signed sum.

## 3. Initial segment and taper

We extend the proof of
[half-grid initial/taper](research_mixed_next_three_half_grid_incoming_initial_taper.md),
retaining its literal cap source and all its finite groups.
On the taper keep
\[
\ell(x)=7/100+x/4\in[19/200,1/8],\qquad
\Im s=h_s,\qquad\text{first aliases }-1/5,+4 .
\tag{10}
\]
The original coupled incoming derivative for every fixed first
profile and regular cap profile is
\[
\Re D_a+\lambda\Im D_a,\qquad
D_a=g'(e+a)+g'(a+s)-2g'(a)+2\pi is .
\tag{11}
\]
It does not contain \(y\). The old fixed-index and moving-cut
transport therefore remains unchanged once its index-force and
current comparisons are verified on (1).

For every real low first index the outgoing shifted real part
lies in \([.45,.625]\); its modulus is at least one for every
positive radius. The incoming folded modulus is at least
\(2\sin\pi v\). Thus the whole low physical block increases
to its cut, including the zero row. At the moving cut the
same forces \(9/5,135/64\) give the derivative \(>1/200\).
On the added main interval \(\ell(x)\le v\le3/20\),
\[
q+v\in[.545,.65],\qquad |1-e^{-2\pi i(y+v+ih_s)}|\ge1 .
\]
The unchanged own squared bound \(D_0<5/6\) and incoming
modulus \(>15/16\) give the same force \(>9/8\).
The main clips upward to \(3/20\), after which the original
incoming transport reaches \(a_0\). The real half does too.

For every retained first-current index \(\ell(x)\le v\le1/2\),
\[
1/2<q+v\le1 .
\tag{12}
\]
The outgoing argument and real cotangent are consequently
nonpositive at all private heights. Section 4 of the cited
half-grid proof uses this sign, not the equality \(q=1/2\),
in all four of its explicit cotangent comparisons. They therefore
give \(\Re Q_{1,ss}<0\) for every \(\sigma\ge h_s\).
The all-height upper bound is still
\[
J_1=\Im Q_{1,s}\le81\pi/100 .
\]
The original upper-height limit is now
\[
\pi(-1-2q+2v)\ge-181\pi/100 .
\tag{13}
\]
Since \(J_1\) decreases, this gives the identical lower bound
above \(h_s\). Both horizontal losses \(119\pi/500\) and
\(28769\pi/50000\), all four weighted-side decreases and both
convex unweighted joins are unchanged. Their endpoint profiles
reach the complete calibration (8).

For the full first upper physical block put \(v=1-t\),
\(J(v)=\int_0^v\log(2\sin\pi s)\,ds\), and subtract its last
rate. The exact rate remains
\[
\Phi(v)=3J(v)
-\int_0^v\log|T-e^{-2\pi i(x-b)}|\,db
-\int_0^v\log|1-Re^{-2\pi i(q-b)}|\,db ,
\quad T=e^{-2\pi\Im a},\quad R=e^{\pi/50}.
\tag{14}
\]
For \(0<v\le9/50\), its outgoing arc is contained in
\([.27,.5]\), so that logarithm is nonnegative. The same
centered incoming inequality gives
\[
\Phi(v)\le3J(v)-2J(v/2)
\le v\{\log(8\pi^2v^2)-2\}<0 .
\tag{15}
\]
For \(9/50\le v\le1/2\), the original correlated incoming
modulus remains \(<21/10\), and the outgoing modulus remains
\(<31/15\). The already proved convex envelope
\[
\Phi(v)-\Phi(1/2)
\le(37/25)(1/2-v)+3J(v)\le0
\tag{16}
\]
is unchanged, including its \(-19/10000\) endpoint witness.
Thus all upper rows reduce to half or last at the current \(q\).
The regular cap plus last transports by the same positive
derivative as equation (25) of that proof: its only shared
term is the constant \(\log R\). The separate true cap-end
alternative also increases along the taper. Every such paired
profile is therefore covered by (8), with either weight in (7).

On the initial segment retain the exact split at \(1/32\).
The complete prefix on \([0,1/32]\) has disk rate \(77/50\)
and outgoing degree at most \(D\), hence fits (9) on the
present top circle. On \([1/32,1/10]\) keep the original
regular cap source, its extra real cap strip \([.49,.5]\),
and first cuts \(19/200,1/2\). Its exact incoming derivative
at every canonical current remains
\[
\log\frac{|1-e^{-2\pi i(e+x)}|
              |e^{-2\pi\sigma}-e^{-2\pi i(x+v)}|}
             {(2\sin\pi x)^2}>\log(11/8).
\tag{17}
\]
It is independent of \(q\), so transports every such current
to \(x=.1\). The extra real cap strip clips to \(e=.49\) there.
The low physical rows obey the same low-index force, and all
upper rows obey (15)--(16). The regular cap itself
increases for its last alternative. The true cap ends times
the complete first kernel retain their disk rate \(389/300\);
the exterior cost \(\pi/50\) still leaves a strict bound below
\(B_f\), so their entire group uses (9).
No compact cap packet is extended to a true private endpoint.

## 4. The right incoming horizontal

Keep the first cuts \(1/20,1/2\), main height \(h_s\), and
aliases \(-1/5,+4\), exactly as in the right half-grid proof.
Its raw low block and real lower cut fit \(B_f\) by the
complete cap ceiling \(3203/3000\), the low rate \(169/400\),
and their strict disk reserve \(299/6000\). Its cap-times-last
envelope retains reserve \(83/4200\) below \(B_f\).
These bounds are independent of \(q\), and (9) pays them.

All remaining first mains and the real half obey the
profilewise upper-endpoint comparison from Section 2.
For their currents, \(x+v,q+v\in[1/2,1]\) on the entire
interval (1). Thus both shifted cotangents are nonpositive,
and the own one is positive for \(v<1/2\).
The first rate is vertically convex at every height, and
the original argument decreases between
\[
2\pi x\le\pi,\qquad
\pi(-1-2q+2v)\ge-19\pi/10 .
\tag{18}
\]
The two horizontal losses remain \(\pi/5\) and
\(1031\pi/5000>\pi/5\). All four weighted sides decrease
away from their real cuts, and both unweighted joins are
bounded by their real and main endpoints. Numerator walls
use the continuous period/reflection upper rate, whose
upward height-derivative jump preserves these comparisons.

The whole first upper physical block reduces to its real
half or last rate by transformed-upper-row Lemma 1, since
\(x,q\in[.45,.5]\) and both absolute heights are less than
\(.108\). This includes its final physical row and every
zero. The half alternative uses the supporting-cap profile
bound; the last alternative uses the complete raw attachment.

## 5. Full finite assembly and the selected denominator

For the canonically decomposed first groups use exactly the
cut \(\ell\) above and the index partition
\[
A_N=\lfloor N\ell\rfloor+1,\quad M_N=\lceil N/2\rceil,\qquad
j<A_N,\quad A_N\le j<M_N,\quad M_N\le j<N .
\tag{19}
\]
The canonical interpolation is the original
\[
e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                         E_N(a)E_N(y)E_N(s)^3 .
\tag{20}
\]
Its exact middle identity keeps \(+N\,ds\), both horizontal
aliases and four weighted sides. Moving the constant mode
retains both unweighted joins. The next factor retains its
complete reduction from Section 2. The low and upper groups
are literal finite products with their actual integer ends.

The same-index current comparisons precede multiplication
by the next controlling profiles and the weight (7).
Every such nonraw pair has reserve \(>1/1000\); all raw
groups use their complete \(B_f\) attachment with gap
\(1/1000\). The uniform zero-safe product and reciprocal
factorial bounds introduce arbitrarily small common
tolerances. At \(q=v=1/2\) the numerator wall is estimated
by its original two-branch period/reflection bound; no
nonzero symbol is required there. Half-grid displacements
cost \(O(\log N)\) in the logarithm. Both parities, every
endpoint row, and all sampling frequencies remain.

The complete forced Fourier estimate is
\[
|d_N(Y)Y^{-N}|
\le C_\tau N^B
 \exp N\{\max(W_{\rm fac}(y),W_{\rm force}(y))+\tau\}.
\tag{21}
\]
Apply both profile comparisons before this maximum is
taken. Choosing all tolerances inside their reserves and
weakening to \(1/10000\) proves (4). The bounded incoming
lengths, original measures \(N\,dx\) and
\(N(1-i\lambda)\,dx\), and all finite sums cost only powers
of \(N\).

Finally, on the entire prescribed top interval,
\[
K_N^\Gamma(y)
=-\frac{N F_N^\Gamma(w,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z)}
          {1-Y^{-N}},\qquad
|1-Y^{-N}|\ge1-e^{-\pi N/50}.
\tag{22}
\]
This proves the density and integral assertions following
(5), retaining both original factors \(N\) and the exact
top-contour sign.

The result concerns the three original unfiltered incoming
paths in (3). The already proved central source, far real
source and old filter correction have their own bounds.
The incoming corner must still be treated as its oriented
union. Nothing here bounds that union or proves cancellation
of the remaining coherent middle insertion.
