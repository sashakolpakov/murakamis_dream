# The Frobenius clock needs a logarithmic internal-centralizer adapter

Independent current-map theorem and audit, 27 October 2026. The
actual Frobenius source gives the correct finite cut clock and a
regular finite approximation to the old physical Springer graph.
It does not identify the internal centralizer coordinate by an
algebraic symplectic map. That coordinate necessarily contains
a logarithm of the source angular flag. The same source Cartan
current has two distinct geometric interpretations, which must
not be conflated.

There is also an exact metric qualification for the controlled
head-shift gauge: its standard-coordinate unitarity does not
give a polynomial bound in the compact coherent metric.

## 1. The actual finite clock graph and its marked flux

Use the r=N actual Frobenius source of
[the two-clock theorem](high_color_two_clock_normal_source.md),
with \(v=t\), \(a=u/(1+tu)\), \(T=va\), and
\(\Omega=dv\wedge da=-dT\wedge d\log v\).
The covariant symbol of the actual operator \(Q_N^{-R}\) is exactly
\[
 F_N(T)=[1+\alpha_NT]^N,\qquad
 \alpha_N=Q_N^{-1}-1,\quad Q_N=e^{c/N},\ c=2\pi i.
\]
On the cyclotomic diagonal source,
\(Q_N^S=Q_N^R\) as OPERATORS, so this is the single symbol of
the inverse head clock. It does not license pointwise products
or inversion of symbols.

Put
\[
 \eta_N=\frac{1-F_N(va)}v,\qquad A_N=F_N^{-1}.
\]
The division by v is polynomially removable at zero.
On the opposite chart \(V=1/v,T'=1-T\),
\[
 F_N(1-T')=[1+(Q_N-1)T']^N,\qquad
 \eta'_N=-v^2\eta_N=\frac{F_N(1-T')-1}{V}.
\]
Thus both pole clutches are retained by an actual algebraic
finite-clock graph. Uniformly on compact complex source sets,
it converges with fixed derivatives to
\((1-e^{-cva})/v\), the earlier physical graph.
This convergence identifies geometric coordinate functions.
Section 6 distinguishes the NEW diagonal position clock from
the OLD physical clock after the actual Fourier/shear source gauge;
they must not be identified merely from the diagonal constraint.

For N>=3 and \(0\le T\le1\),
\[
 \cos^N(\pi/N)\le|F_N(T)|\le1 .
\]
The graph avoids the Gauss wall. In particular its lower bound
is at least 1/8 for every N>=3. Level two is excluded: its chord
passes through zero.

Let \(\Xi=d\log F\wedge d\log v\) on the resolved target.
Its exact pullback is
\[
 \Xi_N=-\frac{N\alpha_N}{1+\alpha_NT}\Omega .
\]
The marked chord logarithm satisfies
\(\Log(Q_N^{-1})=-c/N\). Hence
\[
 \int_{\Gamma_N}\Xi
      =cN\Log(Q_N^{-1})=-c^2=4\pi^2 .                 \tag{1}
\]
This is the same integer wall flux as the old physical cycle.

The explicit continuation is
\[
 \widetilde T_N(T)=-\frac N c\Log(1+\alpha_NT).
\]
It has \(\widetilde T_N(0)=0\), \(\widetilde T_N(1)=1\)
on that marked sheet. The finite graph is the physical graph
evaluated at \((v,\widetilde a_N=\widetilde T_N/v)\).
Its derivative is the nonzero unit
\[
 \widetilde T_N'=-\frac{N\alpha_N}{c(1+\alpha_NT)}
                           =1+O(1/N)
\]
near the real compact cycle. Moreover
\[
 \Phi_N^*\Omega-\Omega
        =d[(T-\widetilde T_N)d\log v].                 \tag{2}
\]
The primitive extends at both pole fibers: its coefficient
vanishes at T=0 and T=1. Thus (2) is a genuine source-form
homotopy near the compact cycle, not a dropped endpoint.
For a nonconstant word kernel its pullback must also transport
that kernel; multiplying the old kernel by the area multiplier
alone is not the same operation.

## 2. An algebraic map to the original two-frame torsor is impossible

The ORIGINAL internal two-frame form is
\[
 \Omega_{\rm cut}=d\tau\wedge d\log A,\qquad
 A=(1+s)^{-1},\quad\tau=r/s .
\]
Fix \(A=A_N(T)\) as above, or the physical limit \(A=e^{cT}\).
Suppose a nonzero form comparison with the compact source is
required, with multiplier depending only on T:
\[
 d\tau\wedge d\log A=\kappa(T)\Omega,\qquad\kappa\ne0 .
\]
Writing \(d\log A=g(T)dT\), with \(g\ne0\), forces
\[
              \partial_v\tau=\frac{\kappa(T)}{g(T)v}. \tag{3}
\]
Thus \(\tau=(\kappa/g)\Log v+\tau_0(T)\) locally.

No single-valued rational or finite-algebraic tau can satisfy (3).
Fix generic T and pass to a place above v=0 on a finite algebraic
cover. The differential of a meromorphic function has zero residue;
the pullback of a nonzero multiple of \(dv/v\) has nonzero residue,
multiplied by the ramification index. This proves the obstruction.

On the MARKED LOG cover, one may instead take
\[
                         \tau=\Log v/c .
\]
Then the exact finite graph gives
\[
 d\tau\wedge d\log A_N=\widetilde T_N'\Omega .
\]
At the physical limit the multiplier is one. The deck
transformation \(\Log v\mapsto\Log v+c\) gives
\(\tau\mapsto\tau+1\): it is precisely a relative centralizer
endpoint, not an algebraic finite-cover identification.
Changing tau by a function of A does not change this two-form;
its poles and branch endpoints remain part of the source.

This identifies the additional torsor needed for the current map:
a logarithmic centralizer with its marked translation and pole
clutches, rather than a single-valued coordinate on a split B1 chart.

## 3. The actual Cartan current has two different geometric images

The actual Frobenius Cartan commutator current is
\[
 X_h=2v\partial_v-2a\partial_a
                         =2\partial_{\log v}\ \text{at fixed T}.
\]
Its Hamiltonian is \(H=1-2T\), with
\(\iota_{X_h}\Omega=-dH=2dT\).
Under the logarithmic centralizer map of Section 2,
\[
                   X_h\longmapsto(2/c)\partial_\tau .
\]
This is a concrete vertical-current match on the marked cover.

By contrast, under the old PHYSICAL SPRINGER map
\(v=1/p\), \(T=\Log A/c\), the SAME current changes the
COMMON DIAGONAL MOMENTUM p and leaves A fixed. That old map
forgets the original internal centralizer coordinate r.
It is therefore not the above identification of the vertical
two-frame current. Restoring momentum and retaining the
centralizer as a separate logarithmic coordinate is essential.

There is an exact finite quantum distinction as well:
\[
 \sigma(\Log Q_N^{-R})=-cT,\qquad
 \Log\sigma(Q_N^{-R})=-c\widetilde T_N .
\]
Their equality holds only at leading N-order. Passing from the
linear actual Cartan moment to a logarithm of the clock symbol
requires the corresponding star/current correction, not ordinary
pointwise functional calculus. Equations (1)--(3) do not erase it.

## 4. The root gauge cost depends on the metric

The controlled source gauge
\(G=\sum_RP_R\otimes V^R\) is a unitary permutation in its
constant coordinate basis. This correctly gives the root
same-color source comparison and does not change any exact
period when all operators, sources, duals and projectors are
transported.

In the compact head's binomial coherent metric the conclusion is
different. Put \(n=N-1\) and use
\(g_s=1/\binom ns\); the dual binomial convention gives the
same condition-number conclusion. For any diagonal metric on the
Frobenius factor, its weight cancels because G fixes R.
Choose a central head s and a block R sending it to head zero.
Then
\[
 \|G\|\ge\sqrt{\binom n{\lfloor n/2\rfloor}} .
\]
The inverse has the same lower bound, by reversing that cycle.
Consequently
\[
 \operatorname{cond}_{\rm coherent}(G)
       \ge\binom n{\lfloor n/2\rfloor}
       \ge\frac{2^n}{n+1}.                            \tag{4}
\]
Thus its standard-metric polynomial cost cannot be imported
into a coherent-metric leading-norm estimate.

This does NOT affect exact gauge invariance or the exact
root equality with K_N. A whole normalized source unit and
near-identity matrix germ are likewise sufficient for exact
same-color identities, but do not give a uniform estimate on
a growing normal neighborhood. Any leading geometric norm
argument must retain its actual metric/source adapter.
The current-map problem has therefore acquired explicit
logarithmic, star, and metric data; none is supplied by an
abstract identification of the two SL2 actions.

## 5. The selected diagonal coupon nevertheless has a tame coherent norm

There is a stronger positive statement for the ACTUAL selected line.
It does not require bounding G on the whole module.
Use the root TENSOR coherent metric
\[
 g_{R,S}=\frac{\binom NR}{\binom{N-1}S}.
\]
The Frobenius numerator is fixed by the actual divided action:
\(F^\dagger=E\) implies
\((R+1)g_{R+1}=(N-R)g_R\), hence
\(g_R=\binom NR\). The head denominator is the existing compact
kernel metric. This is not the binomial metric of one ordinary
color of dimension \(N(N+1)\).

On the selected vectors \(z_k=w_{k,k}\), \(0\le k<N\), and
\(z_N=w_{N,0}\), the actual source and co-source are
\[
 \psi_D=\sum_{k=0}^Nz_k,\qquad
 \lambda_D(z_k)=2^{-N}\binom Nk .
\]
Their pairing is one. Directly,
\[
 \|\psi_D\|^2
   =\sum_{k=0}^{N-1}\frac{\binom Nk}{\binom{N-1}k}+1
   =N\sum_{j=1}^N\frac1j+1,
\]
\[
 \|\lambda_D\|^2
   =4^{-N}
      \left[\sum_{k=0}^{N-1}
             \binom Nk\binom{N-1}k+1\right]
   =\frac{\binom{2N-1}{N-1}+1}{4^N}.                  \tag{5}
\]
The second equality is Vandermonde. Since
\(\binom{2N}{N}/4^N\le1/\sqrt{N+1}\), proved by comparing
successive ratios, and the harmonic sum is at most \(1+\log N\),
the selected rank-one coupon satisfies
\[
 \|e_D\|=\|\psi_D\|\,\|\lambda_D\|
                =O(N^{1/4}\sqrt{1+\log N}).            \tag{6}
\]
The same bound holds for its trace-functional norm.

The source orientation is important. Under the Frobenius
BINOMIAL COORDINATE change
\(D_{\rm Fr}=\operatorname{diag}\binom Nk\), source coefficients
become \(\binom Nk\), dual coefficients become \(2^{-N}\),
and the Frobenius metric becomes \(1/\binom Nk\).
These transform together and reproduce exactly (5);
mixing the old source with the new metric would give a false
exponential factor.

Thus the controlled shear is exponentially conditioned on
the full product space, while its selected coupled coupon
is polynomially bounded in that SAME coherent metric.
This is a useful period-line bound, stronger than a standard
coordinate-norm observation. It still does not control the
whole crossing norm, a growing normal neighborhood, a big-color
coherent metric, or the selected coefficient after the unknown
Gaussian/source comparison.

The tame bound (6) is for the SELECTED anchor, not uniformly for
its entire coherent orbit in this ambient product metric.
Indeed put \(t=u=x\), \(0<x<1\). Then
\[
 \psi_D(x)=\sum_kx^kz_k,\qquad
 \lambda_D(x)(z_k)=\binom Nk
                          \frac{x^k}{(1+x^2)^N}.
\]
Its source norm is at least one. On \(k\le N/2\), the dual
norm numerator satisfies
\[
 \sum_k\binom Nk\binom{N-1}k x^{2k}+x^{2N}
   \ge\frac12\sum_{k\le N/2}\binom Nk^2x^{2k}
   \ge\frac{(1+x)^{2N}}{8(N+1)}.
\]
For the last step, pairing k with N-k shows that the lower
half of \(\sum_k\binom Nkx^k\) is at least half its total;
then apply Cauchy--Schwarz to that half.
Consequently
\[
 \|e_D(x,x)\|
    \ge\frac1{\sqrt{8(N+1)}}
                 \left(\frac{1+x}{1+x^2}\right)^N .
\]
At the actual real coherent point \(x=1/2\) the ratio is 6/5.
Thus the whole real orbit can have an exponential ambient
condition number despite the tame selected anchor.
The intrinsic Fr coherent metric transported by G would
instead make this orbit orthogonal; its comparison with the
ambient product metric is precisely the large adapter that
cannot be discarded.

## 6. The actual polarization changes the physical clock

Let \(A_{\rm old}=Q^S\) be the original head clock and V the
unit cyclic head shift. The actual source gauge is
\(H_0=G(I\otimes\mathcal F)\), with
\(\mathcal F_{s,t}=Q^{st}/N\). Direct finite Fourier calculation gives
\[
 H_0A_{\rm old}H_0^{-1}=V^{-1},\qquad
 H_0V_{\rm old}H_0^{-1}=Q^{-R}Q^S.                   \tag{7}
\]
Thus the OLD physical clock is a NEW SHIFT. The new constraint
\(Q^S=Q^R\) concerns the new POSITION coordinate. The finite
clock graph in Section 1 is an actual new-position source graph,
but (7) prevents identifying it with the old cut observable
without its polarization/source adapter.

This has an exact all-level source test. The diagonal projector P
selects \(z_j=(j,j)\) and \(z_N=(N,0)\). Since V changes S while
fixing R,
\[
                         PV^{-1}P=0.
\]
Hence every Frobenius coherent source supported on P has zero
expectation of the transformed OLD clock V^{-1}.
Its expectation of the NEW diagonal clock \(Q^R=Q^S|_P\)
is instead the nonconstant binomial function of T.
These actual moments are different at root order, even though
the unweighted closed knot matrix is scalar.

The root generating kernel is
\(N^{-1}Q^{s_{\rm old}(s_{\rm new}-R)}\).
On marked logarithmic coordinates its canonical phase is
\[
 W=q_{\rm old}(q_{\rm new}-q_R).
\]
With the usual stationary transform convention,
\[
 p'_{\rm head}=q_{\rm old},\quad
 p_{\rm old}=q_R-q_{\rm new},\quad
 p'_R=p_R-q_{\rm old}.
 \tag{8}
\]
For the source \(\psi(t)\), the coupled conormal relation is
\(p'_R+p'_{\rm head}=\Log t\). This is a Fourier/Legendre
polarization change, not the equality of the two position clocks.
Its whole q-germ is still the supplied finite matrix gauge;
a root generating phase alone does not specify all its q-jets.

There is a useful exact NEUTRAL CURRENT formed from the charged
physical clock. In the new factor coordinates,
\[
 \widetilde E=(e_{\rm Fr}\otimes I)V^{-1},\qquad
 \widetilde F=(f_{\rm Fr}\otimes I)V .
\]
These are precisely the actual endpoint-completed ladders built
from divided powers and the first-normal wrap arrows.
They commute with P and have the nonzero Fr coherent Hamiltonians.
Bare \(V^{-1}\) does not preserve P; dressing it by the divided
generator compensates its charge. Thus the old clock can enter
the coupled current complex as a charged correspondence whose
neutral dressed version is observable. This is an actual
finite-source identity, not yet the full geometric current map.

The whole lift of the original position clock matters too.
For \(C_Q=Q^SZ^R=Q^J\),
\[
 [e(q),C_Q]/\delta\longrightarrow-A_{\rm head}e_0,\qquad
 [f(q),C_Q]/\delta\longrightarrow A_{\rm head}f_0 .
\]
In contrast the reduced head clock \(Q^S\) commutes with these
divided operators for every q. The scaled commutator is therefore
a statement about the specified NORMAL LIFT, not its root value.
It is not a regular derivation on the whole Fr algebra:
\([e,f]\) already has nonzero root value. All source, charged
neighbor, and endpoint components must remain in that comparison.

The subsequent [unprojectivized actual source theorem](actual_unprojectivized_frobenius_borel_torsor.md)
retains the missing scale rather than forcing a constant-generator
identification through the normalized quadric. On its marked paired
source cover, two actual Borel fields map to the internal framing
fields, and the actual scale U plus one descendant m give
Omega_cut=(A/N)dlog U wedge dm. The old-clock normal pairing above
detects U. This repairs that source/framing moment problem; it does
not turn the two root clock observables into the same operator or
construct the remaining whole network/Gaussian current map.

## 7. The selected coupled source is orthogonal in a hybrid metric

The metric in Section 5 is the tensor product of TWO classical
coherent metrics. There is another useful, explicit metric on the
same actual source: keep the Fr coherent metric and the original
flat head metric,
\[
                 g_{R,S}=\binom NR .                 \tag{9}
\]
This is a different norm statement; it does not alter any of the
conditioning results in the earlier metric. At the marked root,
G sends (R,S) to (R,S+R mod N). It preserves (9) exactly. The
actual Fourier matrix F_(S,T)=Q_N^(ST)/N has
F^*F=I/N, so H_0=G(I tensor F) is a scalar N^(-1/2) times a
unitary map in (9). Its condition number is ONE. Conjugation by
H_0 is isometric on both the operator and Hilbert--Schmidt norms.
These statements concern the ORIGINAL finite Fourier adapter,
including its 1/N; it has not been replaced by a different source.

The original source coupon e_+ tensor e_h is an orthogonal
rank-one projector in this metric. Its transported coupled coupon
is likewise orthogonal. Explicitly, with s(R)=R mod N,
\[
 \psi_D=\sum_{R=0}^N v_R\otimes e_{s(R)},\qquad
 \lambda_D(v_R\otimes e_S)=2^{-N}\binom NR\delta_{S,s(R)}.
\]
Thus
\[
       \|\psi_D\|^2=2^N,\qquad
       \|\lambda_D\|_*^2=2^{-N},\qquad\|e_D\|=1.  \tag{10}
\]
In particular |Phi_D(T)|<=||T|| for every actual inserted matrix
in this specified metric. This does not estimate the norm of the
full crossing word or its geometric block. The head factorial
gauge in degree elevation is not automatically isometric in (9).
No bound on its full whole-q source transport is inferred.

The highest-spin Fr projection is orthogonal for the induced
Hilbert--Schmidt norm. Consequently it remains a contraction after
conjugation by H_0. On b fixed strands, a projected inserted matrix
has source pairing bounded by its Hilbert--Schmidt norm, hence by
the square root of the ambient dimension times its operator norm.
This costs a power of N, while the operator's own size remains to
be proved. It is a selected-source estimate at the root, not a
uniform estimate on the full Borel orbit or a moving-q neighborhood.

## 8. A normalized highest-spin clock residue and the source character

There is a direct normalization check for the boundary polynomial
in [the highest-spin quotient](degree_elevation_complement_bockstein_wall.md).
On the Fr leg put
\[
 B_0=\operatorname{diag}_{R=0}^N((-1)^R\binom NR),\qquad
                       U_z=\operatorname{diag}(z^R).
\]
B_0 is the weight-zero vector in the highest adjoint spin N:
the adjoint Casimir has eigenvalue 2N(N+1). Its squared
Hilbert--Schmidt norm is binom(2N,N). Since U_z has weight zero,
its entire highest-spin component is EXACTLY
\[
        P_{W_N}(U_z)=\frac{(1-z)^N}{\binom{2N}N}B_0. \tag{11}
\]
The unnormalized obstruction polynomial is (1-z)^N u^N. Formula
(11) retains the conversion to the actual coherent operator norm.
For |z|=1 it gives
\[
 \|P_{W_N}(U_z)\|_{HS}
       =\frac{|1-z|^N}{\sqrt{\binom{2N}N}}
       \le\sqrt{2N+1}.                             \tag{12}
\]
The last bound follows from binom(2N,N)>=4^N/(2N+1). An
unnormalized factor 2^N in the obstruction polynomial is therefore
not by itself an exponential operator-norm obstruction.

The SOURCE comparison on the surviving endpoint is different.
For the normalized endpoint W=f^N/N!=E_(N,0),
\[
 \Phi_{\rm Fr,uniform}(W)=\frac1{N+1},\qquad
 \lambda_+ W\psi_+=2^{-N},\qquad
 \Phi_D(W\otimes H)=2^{-N}H_{00}.                  \tag{13}
\]
In the actual paired Borel family the last coefficient is
((1-m)/2)^N H_00. Its integral over dm/2 from -1 to 1 is
H_00/(N+1), whereas its selected value at m=0 is 2^(-N)H_00.
The exact ratio 2^N/(N+1) must remain in a source comparison.
At the root W is closed for the MEMORY Cartan/F complex, so
these two rows cannot differ by a Ward coboundary on the full
target. The previously proved head-cut homotopy applies on the
degree-elevation IMAGE; it does not justify replacing this extra
endpoint row. The actual physical clock still has the distinct
polarization dictionary in Section 6.

Indeed even in (9) the uniform Fr coupon has squared norm
\[
 \|\psi_+\lambda_{\rm uniform}\|^2
       =\frac{2^N}{(N+1)^2}\sum_{R=0}^N\binom NR^{-1}
       \ge\frac{2^{N+1}}{(N+1)^2}.                 \tag{14}
\]
This does not prevent cancellations in its interval period.
It prevents treating its replacement of the selected coherent
row as a tame source gauge without the full character/period
calculation. The tame Fourier/controlled change (9)--(10) and
the distinct interval-source character (13)--(14) are separate
exact statements.

[The exact matrix and source audit](../experiments/audit_highest_spin_cutoff_and_hybrid_metric.py)
checks the coherent highest-spin normalization, actual coupled
source/Fourier metric, endpoint character and the PBW pole cutoff.

