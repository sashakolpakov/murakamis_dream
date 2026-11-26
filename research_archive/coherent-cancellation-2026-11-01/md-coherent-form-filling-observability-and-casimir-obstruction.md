# The exact filling-family Gram and its failure under a Casimir insertion

1 November 2026. Private finite algebra. No closed-source realization,
source-volume bound, or new manuscript theorem is asserted.

## 1. Coverage and the question being isolated

The existing actual_filling_fourier_hermite_gram note already constructs a
positive full-rank coherent metric for the entire mixed-color packet,
with polynomial conditioning and exact dual filling cost
\(1+n^2(N^2-1)/(12N^2)\). Its explicit source examples show why that
energy is not automatically the filled-volume energy. The
actual_pointed_metric_transport_and_crossing_obstruction note also gives
the general moving-metric and adjoint-residual identities. Neither
construction is repeated here. The actual_adjacent_observable_source_filtration
note, section 3, already excludes a nontrivial source-preserving quotient
invariant under both actual adjacent Casimirs on the physical multiplicity
module. The present result concerns a different, smaller scalar spectral
coefficient space: it explicitly identifies the all-twist observable form
and an infinite-level collision kernel that one Casimir insertion detects.
It is not offered as a new general no-quotient principle.

The narrow question here is whether one may instead retain only the data
seen by all scalar twist fillings at one spectral port, and propagate that
smaller positive form through a source manipulation. The answer is
negative for multiplication by the actual Casimir, at infinitely many
even composite levels. The obstruction is exact, with no asymptotics.

All local formulas below use the original full-Hermite normalization in
actual_uniform_filling_supremum_bound, equations (8)–(14). The source
application begins at \(N\ge3\); the scalar algebra is meaningful at \(N=2\).

## 2. An explicit observable quotient for the entire filling family

Set \(d=N-1\), \(q=e^{\pi i/N}\), \(m=\lfloor N/2\rfloor\), and
\[
 \phi_a=(2a+1)\pi/N,\quad c_a=2\cos\phi_a,\quad 0\le a<m.
\]
These are the distinct double roots of \(\chi_N(z)=2T_N(z/2)+2\).
When \(N\) is odd there is also the simple node \(-2\), indexed by \(a=m\).

For a polynomial \(H\) of degree at most \(d\), define at each double node
\[
 \alpha_a(H)=\frac{(4-c_a^2)H'(c_a)-c_aH(c_a)}{N^2},
 \qquad
 \beta_a(H)=\frac{i(\pi-\phi_a)\sin\phi_a}{\pi N}H(c_a).
 \tag{1}
\]
At the odd simple node set \(\alpha_m(H)=H(-2)/N^2\),
\(\beta_m(H)=0\). The coefficient of \(n\) in (1) follows directly by
differentiating the original Gaussian multiplier:
\[
 \frac{f_n'(c_a)}{f_n(c_a)}
 =\frac{inN(\pi-\phi_a)}{4\pi\sin\phi_a}.
\]
Here the prime is in the spectral variable, not in \(\phi\).

Put
\[
 \mu_N=q^{d^2/2},\qquad k_a=a(a-d)\pmod{2N},\qquad
 \lambda_a=q^{k_a}.
\]
For every signed integer \(n\), including negative powers, the original
nodal multiplier is \(f_n(c_a)=\mu_N^n\lambda_a^n\).
This also holds at the odd simple node. Thus, with empty sums zero, define
\[
 A_k=\sum_{a:k_a=k}\alpha_a,\qquad
 B_k=\sum_{a:k_a=k}\beta_a,\qquad 0\le k<2N.
\]
The full functional is exactly
\[
 \mu_N^{-n}\mathcal L_N^nH
      =\sum_{k=0}^{2N-1}q^{kn}(A_k+nB_k).
 \tag{2}
\]
Every original root phase and normal is retained. Equal phases at
different Casimir nodes are grouped before a modulus is taken.

Let \(L=2N\) and \(Y_n=\mu_N^{-n}\mathcal L_N^nH\). The two consecutive
periods recover the grouped data by an ordinary finite Fourier transform:
\[
 D_j=\frac{Y_{j+L}-Y_j}{L}=\sum_kq^{kj}B_k,\qquad
 E_j=Y_j-jD_j=\sum_kq^{kj}A_k,\quad 0\le j<L.
 \tag{3}
\]
Consequently
\[
 \mathcal E_N(H)=\sum_k(|A_k|^2+N^2|B_k|^2)
   =\frac1{2N}\sum_{j=0}^{2N-1}(|E_j|^2+N^2|D_j|^2)
 \tag{4}
\]
is an explicit positive semidefinite Hermitian form. Its kernel is exactly
the polynomials invisible to every integral twist filling. Equations
(1) and (4) define the form directly from finite nodal data; the Fourier
identity is a verification, not a definition using an unknown invariant.

If \(r_N\) is the number of occupied phase classes, Cauchy gives
\[
 |\mathcal L_N^nH|^2
       \le r_N(1+n^2/N^2)\mathcal E_N(H),\qquad
 r_N\le\lceil N/2\rceil.
 \tag{5}
\]
For a fixed number of ports, the tensor product form gives the product of
these polynomial costs on the whole shared polynomial. This is a finite
norm statement. No geometric bound on that form is supplied.

For a node-vanishing \(H\), every \(B_k\) is zero. Then (4) simplifies to
\[
 \mathcal E_N(H)=\frac1{2N}\sum_{n=0}^{2N-1}
                         |\mathcal L_N^nH|^2.
 \tag{6}
\]
Thus the quotient really keeps all twist-observable interference, rather
than imposing a diagonal norm on individual node contributions.

## 3. An infinite-level obstruction to propagation through multiplication

Take \(N=8r+2\), \(r\ge1\), and write \(m=N/2=4r+1\). Set
\(c=2\cos(\pi/N)>0\). The first and last double nodes are \(c_0=c\)
and \(c_{m-1}=-c\). Their reduced phase exponents agree:
\[
 (m-1)((m-1)-d)=-m(m-1)=-r(2N).
 \tag{7}
\]
Therefore \(f_n(c)=f_n(-c)\) for every signed integer \(n\), with the
same original common lift \(\mu_N^n\).

Define the two actual left diagonal coefficient polynomials
\[
 h_+(z)=\frac{\chi_N(z)}{z-c},\qquad
 h_-(z)=\frac{\chi_N(z)}{z+c},\qquad H=h_+-h_- .
 \tag{8}
\]
They are respectively the local coefficients of
\(b^0c_{\rm face}^{d}\) and \(b^{m-1}c_{\rm face}^{m}\).
The notation \(c_{\rm face}\) denotes the output middle face variable,
not the spectral node \(c\). Both monomials lie in the genuine left
range. Their unused-row products and original scalar are exact.

The top terms of \(h_+\) and \(h_-\) cancel, so \(H\) has degree \(d-1\).
The full-Hermite resolvent reproduction gives
\[
 \mathcal L_N^nH=f_n(c)-f_n(-c)=0.
 \tag{9}
\]
But there is an exact polynomial identity, requiring no reduction,
\[
 zH=c(h_++h_-).
\]
It follows that
\[
 \mathcal L_N^n(zH)=2c\,f_n(c)\ne0,\qquad
 \mathcal E_N(H)=0,\quad \mathcal E_N(zH)=4c^2>0 .
 \tag{10}
\]
Both \(H\) and \(zH\) have degree at most \(d\).

Hence there is no finite constant \(C_N\) satisfying
\[
 \mathcal E_N(zH)\le C_N\mathcal E_N(H)
 \tag{11}
\]
on the one-sided coefficient space at these levels. More generally,
any positive semidefinite form whose kernel is precisely the common
kernel of the scalar filling family has the same obstruction. Multiplying
by \(z\) is the spectral operation corresponding to retaining an actual
Casimir insertion; this is not a newly chosen nonlinear observable.

This does not assert that (8), with its two different face degrees,
is the shared coefficient of one fixed closed diagram. The conclusion
is about a source-independent interface on the entire literal local
coefficient space. A physical exterior might impose additional
restrictions; those would have to be stated and proved.

## 4. The minimal additional data for this interface

Let \(\mathcal W_N=Z_N\mathbb C[z]_{\le m-1}\) be the one-sided scalar
space, where \(Z_N\) is the polynomial vanishing at every distinct
spectral node. The polynomials \(h_a=\chi_N/(z-c_a)\), \(0\le a<m\),
form a basis. For \(H=\sum_a t_ah_a\),
\[
 \mathcal L_N^nH=\sum_at_af_n(c_a).
\]
The twist family alone remembers only the sums of \(t_a\) over equal
crossing phases.

If one must also preserve arbitrary polynomial Casimir spectators, the
common kernel becomes zero. Indeed
\[
 \mathcal L_N^0(z^jH)=\sum_a t_ac_a^j,\qquad 0\le j<m,
 \tag{12}
\]
where products of larger degree may equivalently be canonically reduced.
The distinct-node Vandermonde matrix is invertible, so all these
pairings vanish only when \(t_a=0\) for every \(a\).

Thus a semidefinite local form that is stable under all such spectators
and controls the original scalar functional cannot discard any
one-sided direction. To see this without assuming (12) is a norm:
bounded multiplication makes its kernel invariant under \(z\);
bounded scalar evaluation makes the kernel lie in \(\ker\mathcal L_N^0\);
then (12) forces that kernel to be zero.

This is a lower requirement on information, not an exponential lower
bound on every positive metric. Full positive non-diagonal forms and
forms retaining common boundary degree registers remain possible.
The result does not exclude controlled anisotropy, coherent contraction
of a larger block first, or estimates on an explicitly smaller physical
set of exteriors.

## 5. Relation to the two known obstructions

The endpoint-locality polynomial in md-general-sector-source-review is
not invisible to odd twist powers: its exact output is of order \(N^{-1}\),
despite exponential smallness on a negative-endpoint disk. The form (4)
therefore does not remove that example by declaring it null.

The R54 result rules out positive diagonal Cauchy weights on its original
local array partition. The form (4) groups genuine equal-phase
contributions and is not diagonal on that partition. Nevertheless
(8)–(11) show why even this more coherent quotient does not by itself
supply a composable planar-source norm. It has to be supplemented by
spectator/boundary information or applied only after a justified coherent
block contraction. No claimed filled-volume comparison follows here.

## Input hashes

- /private/tmp/murakamis_dream-publication/notes/actual_uniform_filling_supremum_bound.md: 372915a7be462b9487b6d5ca9b1132fb25a5d1a0dbbef57406981659513139ca
- /private/tmp/murakamis_dream-publication/notes/actual_filling_fourier_hermite_gram.md: 9345e275c4c086b5f18ff2ded0f78e41e700a58b601bebd4b5e953f64e1b0d88
- /private/tmp/murakamis_dream-publication/notes/actual_pointed_metric_transport_and_crossing_obstruction.md: 46a0109371f7e39438232e059a8de9708734a68439b5b610b78ce78fd1faf392
- /private/tmp/murakamis_dream-publication/notes/actual_complete_source_krein_and_cauchy_metric.md: 83ca3c3838b6ba50ac665bc0c97ed44483040d191de3e38cf647bbdd76acbd4b
- /private/tmp/md-general-sector-source-review.md: 2424c27ce99d8176eb575d3b30830914ed624df4b7f8d6799235da1f81859360
- /private/tmp/murakamis_dream-publication/notes/research_absolute_source_cancellation_obstruction.md: c3ef6983692802da89dcf7d7ec4ad067c07050fdb6c9e6cac70f60cf48955894
- /private/tmp/murakamis_dream-publication/notes/actual_adjacent_observable_source_filtration.md: c115426182ba06c5db16fc1c3292dabfdec187182c4666aacd53b91e13073f44
